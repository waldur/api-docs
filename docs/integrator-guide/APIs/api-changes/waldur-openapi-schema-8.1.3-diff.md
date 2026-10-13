# OpenAPI schema diff - 8.1.3

## For version 8.1.3

### New Endpoints: 170

----------------------
POST /_matrix/app/v1/ping  
GET /api-auth/default/init/  
POST /api/call-reviewer-pools/{uuid}/resend-invitation/  
GET /api/call-rounds/dashboard-deadlines/  
HEAD /api/call-rounds/dashboard-deadlines/  
GET /api/call-workflow-step-notification-rules/  
HEAD /api/call-workflow-step-notification-rules/  
POST /api/call-workflow-step-notification-rules/  
DELETE /api/call-workflow-step-notification-rules/{uuid}/  
GET /api/call-workflow-step-notification-rules/{uuid}/  
PATCH /api/call-workflow-step-notification-rules/{uuid}/  
PUT /api/call-workflow-step-notification-rules/{uuid}/  
GET /api/changelog-entries/  
GET /api/changelog-upgrade-report/  
GET /api/changelog/compare/{from_version}/{to_version}/  
GET /api/changelog/pending/  
GET /api/changelog/releases/  
GET /api/changelog/{version}/  
GET /api/changelog/{version}/delta/  
GET /api/customers/{uuid}/providers/  
GET /api/debug/email/config/  
POST /api/debug/email/probe/  
POST /api/debug/email/send_test/  
GET /api/marketplace-metric-breakdown/  
GET /api/marketplace-metric-definitions/  
HEAD /api/marketplace-metric-definitions/  
POST /api/marketplace-metric-definitions/  
DELETE /api/marketplace-metric-definitions/{uuid}/  
GET /api/marketplace-metric-definitions/{uuid}/  
PATCH /api/marketplace-metric-definitions/{uuid}/  
PUT /api/marketplace-metric-definitions/{uuid}/  
GET /api/marketplace-metric-goals/  
HEAD /api/marketplace-metric-goals/  
POST /api/marketplace-metric-goals/  
DELETE /api/marketplace-metric-goals/{uuid}/  
GET /api/marketplace-metric-goals/{uuid}/  
PATCH /api/marketplace-metric-goals/{uuid}/  
PUT /api/marketplace-metric-goals/{uuid}/  
POST /api/marketplace-metric-points/  
GET /api/marketplace-metric-retention-policies/  
HEAD /api/marketplace-metric-retention-policies/  
POST /api/marketplace-metric-retention-policies/  
DELETE /api/marketplace-metric-retention-policies/{uuid}/  
GET /api/marketplace-metric-retention-policies/{uuid}/  
PATCH /api/marketplace-metric-retention-policies/{uuid}/  
PUT /api/marketplace-metric-retention-policies/{uuid}/  
GET /api/marketplace-metric-series/  
GET /api/marketplace-offering-merges/  
HEAD /api/marketplace-offering-merges/  
POST /api/marketplace-offering-merges/  
GET /api/marketplace-offering-merges/suggest_mapping/  
DELETE /api/marketplace-offering-merges/{uuid}/  
GET /api/marketplace-offering-merges/{uuid}/  
PATCH /api/marketplace-offering-merges/{uuid}/  
GET /api/marketplace-offering-merges/{uuid}/affected/  
POST /api/marketplace-offering-merges/{uuid}/execute/  
POST /api/marketplace-offering-merges/{uuid}/preview/  
POST /api/marketplace-offering-merges/{uuid}/undo/  
GET /api/marketplace-offering-metrics/  
HEAD /api/marketplace-offering-metrics/  
POST /api/marketplace-offering-metrics/  
DELETE /api/marketplace-offering-metrics/{uuid}/  
GET /api/marketplace-offering-metrics/{uuid}/  
PATCH /api/marketplace-offering-metrics/{uuid}/  
PUT /api/marketplace-offering-metrics/{uuid}/  
POST /api/marketplace-offering-metrics/{uuid}/archive/  
POST /api/marketplace-offering-metrics/{uuid}/pause/  
POST /api/marketplace-offering-metrics/{uuid}/purge/  
POST /api/marketplace-offering-metrics/{uuid}/resume/  
GET /api/marketplace-orders/dashboard-my-orders/  
HEAD /api/marketplace-orders/dashboard-my-orders/  
POST /api/marketplace-posix-id-pools/{uuid}/repoint/  
GET /api/marketplace-posix-id-pools/{uuid}/repoint_preview/  
GET /api/marketplace-project-metrics/  
GET /api/marketplace-provider-resources/{uuid}/robot_account_users/  
POST /api/marketplace-resource-api-keys/  
GET /api/marketplace-resource-api-keys/usage_totals/  
HEAD /api/marketplace-resource-api-keys/usage_totals/  
DELETE /api/marketplace-resource-api-keys/{uuid}/  
PATCH /api/marketplace-resource-api-keys/{uuid}/  
POST /api/marketplace-resource-api-keys/{uuid}/pause/  
POST /api/marketplace-resource-api-keys/{uuid}/report_usage/  
POST /api/marketplace-resource-api-keys/{uuid}/resume/  
POST /api/marketplace-resource-api-keys/{uuid}/retry/  
POST /api/marketplace-resource-api-keys/{uuid}/set_deleted/  
POST /api/marketplace-resource-api-keys/{uuid}/set_ok/  
POST /api/marketplace-resource-api-keys/{uuid}/set_paused/  
GET /api/marketplace-resource-metrics/  
GET /api/marketplace-service-provider-accounts/  
HEAD /api/marketplace-service-provider-accounts/  
DELETE /api/marketplace-service-provider-accounts/{uuid}/  
GET /api/marketplace-service-provider-accounts/{uuid}/  
PATCH /api/marketplace-service-provider-accounts/{uuid}/  
PUT /api/marketplace-service-provider-accounts/{uuid}/  
GET /api/marketplace-service-provider-project-groups/  
HEAD /api/marketplace-service-provider-project-groups/  
POST /api/marketplace-service-provider-project-groups/  
GET /api/marketplace-service-provider-project-groups/adoptable_projects/  
HEAD /api/marketplace-service-provider-project-groups/adoptable_projects/  
POST /api/marketplace-service-provider-project-groups/import_groups/  
GET /api/marketplace-service-provider-project-groups/{uuid}/  
POST /api/marketplace-service-provider-project-groups/{uuid}/set_gid/  
POST /api/marketplace-service-providers/{uuid}/account_options_preview/  
POST /api/marketplace-service-providers/{uuid}/adopt_provider_accounts/  
GET /api/marketplace-service-providers/{uuid}/glauth_tree/  
GET /api/marketplace-service-providers/{uuid}/glauth_users_config/  
GET /api/marketplace-service-providers/{uuid}/username_conflicts/  
GET /api/marketplace-software-catalogs/{uuid}/cpu_targets/  
POST /api/matrix/credentials/password/  
POST /api/matrix/credentials/recovery-key/  
POST /api/matrix/crypto/escrow/  
POST /api/matrix/crypto/lease/  
POST /api/matrix/crypto/lease/release/  
POST /api/matrix/rooms/{uuid}/open/  
POST /api/matrix/session/  
POST /api/openportal-unmanaged-projects/{uuid}/set_slug/  
POST /api/openstack-instances/{uuid}/console_log/  
POST /api/openstack-instances/{uuid}/set_metadata/  
POST /api/otlp/v1/metrics/  
GET /api/passkeys/  
HEAD /api/passkeys/  
POST /api/passkeys/mfa/begin/  
POST /api/passkeys/mfa/finish/  
POST /api/passkeys/registration/begin/  
POST /api/passkeys/registration/finish/  
POST /api/passkeys/signin/begin/  
POST /api/passkeys/signin/finish/  
GET /api/passkeys/{uuid}/  
PATCH /api/passkeys/{uuid}/  
PUT /api/passkeys/{uuid}/  
POST /api/passkeys/{uuid}/revoke/  
POST /api/projects/{uuid}/set_slug/  
GET /api/proposal-proposals/dashboard-stats/  
GET /api/proposal-proposals/{uuid}/awarded_resources/  
POST /api/proposal-proposals/{uuid}/awarded_resources/  
DELETE /api/proposal-proposals/{uuid}/awarded_resources/{obj_uuid}/  
GET /api/proposal-proposals/{uuid}/awarded_resources/{obj_uuid}/  
PATCH /api/proposal-proposals/{uuid}/awarded_resources/{obj_uuid}/  
PUT /api/proposal-proposals/{uuid}/awarded_resources/{obj_uuid}/  
POST /api/proposal-proposals/{uuid}/reopen_decision/  
GET /api/proposal-protected-calls/dashboard-stats/  
POST /api/proposal-protected-calls/import_call/  
GET /api/proposal-protected-calls/{uuid}/export-proposals/  
GET /api/proposal-protected-calls/{uuid}/export-reviews/  
POST /api/proposal-protected-calls/{uuid}/export_call/  
POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/complete/  
POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/publish_results/  
POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/record_adoption/  
POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/start_deciding/  
GET /api/proposal-reviews/dashboard-stats/  
GET /api/roles/hygiene_report/  
HEAD /api/roles/hygiene_report/  
GET /api/sram-groups/  
HEAD /api/sram-groups/  
GET /api/sram-groups/{uuid}/  
GET /api/sram-project-rules/  
HEAD /api/sram-project-rules/  
POST /api/sram-project-rules/  
DELETE /api/sram-project-rules/{uuid}/  
GET /api/sram-project-rules/{uuid}/  
PATCH /api/sram-project-rules/{uuid}/  
PUT /api/sram-project-rules/{uuid}/  
GET /api/sram-project-rules/{uuid}/preview/  
GET /api/staff-passkeys/  
HEAD /api/staff-passkeys/  
POST /api/staff-passkeys/{uuid}/revoke/  
POST /api/support-issues/{uuid}/set_status/  
GET /api/users/dashboard-general-stats/  
GET /api/users/dashboard-pending-actions/  
POST /api/web-shell-ticket/  

### Deleted Endpoints: 82

-------------------------
POST /api/assignment-batches/  
POST /api/assignment-items/  
GET /api/azure-images/  
HEAD /api/azure-images/  
GET /api/azure-images/{uuid}/  
GET /api/azure-locations/  
HEAD /api/azure-locations/  
GET /api/azure-locations/{uuid}/  
GET /api/azure-public-ips/  
HEAD /api/azure-public-ips/  
POST /api/azure-public-ips/  
DELETE /api/azure-public-ips/{uuid}/  
GET /api/azure-public-ips/{uuid}/  
PATCH /api/azure-public-ips/{uuid}/  
PUT /api/azure-public-ips/{uuid}/  
POST /api/azure-public-ips/{uuid}/pull/  
POST /api/azure-public-ips/{uuid}/set_erred/  
POST /api/azure-public-ips/{uuid}/set_ok/  
POST /api/azure-public-ips/{uuid}/unlink/  
GET /api/azure-resource-groups/  
HEAD /api/azure-resource-groups/  
GET /api/azure-resource-groups/{uuid}/  
GET /api/azure-sizes/  
HEAD /api/azure-sizes/  
GET /api/azure-sizes/{uuid}/  
GET /api/azure-sql-databases/  
HEAD /api/azure-sql-databases/  
POST /api/azure-sql-databases/  
DELETE /api/azure-sql-databases/{uuid}/  
GET /api/azure-sql-databases/{uuid}/  
PATCH /api/azure-sql-databases/{uuid}/  
PUT /api/azure-sql-databases/{uuid}/  
POST /api/azure-sql-databases/{uuid}/pull/  
POST /api/azure-sql-databases/{uuid}/set_erred/  
POST /api/azure-sql-databases/{uuid}/set_ok/  
POST /api/azure-sql-databases/{uuid}/unlink/  
GET /api/azure-sql-servers/  
HEAD /api/azure-sql-servers/  
POST /api/azure-sql-servers/  
DELETE /api/azure-sql-servers/{uuid}/  
GET /api/azure-sql-servers/{uuid}/  
PATCH /api/azure-sql-servers/{uuid}/  
PUT /api/azure-sql-servers/{uuid}/  
POST /api/azure-sql-servers/{uuid}/create_database/  
POST /api/azure-sql-servers/{uuid}/pull/  
POST /api/azure-sql-servers/{uuid}/set_erred/  
POST /api/azure-sql-servers/{uuid}/set_ok/  
POST /api/azure-sql-servers/{uuid}/unlink/  
GET /api/azure-virtualmachines/  
HEAD /api/azure-virtualmachines/  
POST /api/azure-virtualmachines/  
DELETE /api/azure-virtualmachines/{uuid}/  
GET /api/azure-virtualmachines/{uuid}/  
PATCH /api/azure-virtualmachines/{uuid}/  
PUT /api/azure-virtualmachines/{uuid}/  
POST /api/azure-virtualmachines/{uuid}/pull/  
POST /api/azure-virtualmachines/{uuid}/restart/  
POST /api/azure-virtualmachines/{uuid}/set_erred/  
POST /api/azure-virtualmachines/{uuid}/set_ok/  
POST /api/azure-virtualmachines/{uuid}/start/  
POST /api/azure-virtualmachines/{uuid}/stop/  
POST /api/azure-virtualmachines/{uuid}/unlink/  
POST /api/call-assignment-configurations/  
POST /api/marketplace-openstack-duplicate-offerings/remediate/  
GET /api/slurm-allocation-user-usage/  
HEAD /api/slurm-allocation-user-usage/  
GET /api/slurm-allocation-user-usage/{id}/  
GET /api/slurm-allocations/  
HEAD /api/slurm-allocations/  
POST /api/slurm-allocations/  
DELETE /api/slurm-allocations/{uuid}/  
GET /api/slurm-allocations/{uuid}/  
PATCH /api/slurm-allocations/{uuid}/  
PUT /api/slurm-allocations/{uuid}/  
POST /api/slurm-allocations/{uuid}/pull/  
POST /api/slurm-allocations/{uuid}/set_erred/  
POST /api/slurm-allocations/{uuid}/set_limits/  
POST /api/slurm-allocations/{uuid}/set_ok/  
POST /api/slurm-allocations/{uuid}/unlink/  
GET /api/slurm-associations/  
HEAD /api/slurm-associations/  
GET /api/slurm-associations/{uuid}/  

### Modified Endpoints: 472

---------------------------
POST /api-auth/password/

- Responses changed
  - Modified response: 401
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - Deleted security requirements: waldurTokenAuth
  - Deleted security requirements: waldurPATAuth
  - Deleted security requirements: waldurOIDCAuth

POST /api/admin/matrix-appservice/setup/

- Description changed from 'Generates fresh appservice tokens (rotating any existing ones), enables the appservice, and returns registration YAML.' to 'Generates fresh appservice tokens (rotating any existing ones), enables the appservice, and returns registration YAML. Returns 409 when the deployment owns the tokens; see MATRIX_TOKENS_MANAGED_BY.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: homeserver_domain
            - Description changed from 'Matrix homeserver server_name domain. Only persisted if MATRIX_HOMESERVER_DOMAIN is not already configured.' to 'Matrix homeserver server_name domain. Only persisted if MATRIX_HOMESERVER_DOMAIN is not already configured; a different value is refused.'
          - Modified property: homeserver_public_url
            - Description changed from 'Optional. Matrix homeserver URL used by browser clients. Leave blank when the homeserver URL above is reachable from both servers and browsers. Set this for deployments where the two differ (e.g. Docker-internal vs. Caddy-proxied). Only persisted if MATRIX_HOMESERVER_PUBLIC_URL is not already configured.' to 'Optional. Matrix homeserver URL used by browser clients. Leave blank when the homeserver URL above is reachable from both servers and browsers. Set this for deployments where the two differ (e.g. Docker-internal vs. Caddy-proxied). Only persisted if MATRIX_HOMESERVER_PUBLIC_URL is not already configured; a different value is refused.'
          - Modified property: homeserver_url
            - Description changed from 'Matrix homeserver base URL. Only persisted if MATRIX_HOMESERVER_URL is not already configured.' to 'Matrix homeserver base URL. Only persisted if MATRIX_HOMESERVER_URL is not already configured; a different value is refused.'
          - Modified property: user_registration_secret
            - Description changed from 'Shared secret configured in the homeserver for user registration. Only persisted if MATRIX_USER_REGISTRATION_SECRET is not already configured.' to 'Registration token the homeserver requires for sign-up (its registration_token). Only persisted if MATRIX_USER_REGISTRATION_SECRET is not already configured; a different value is refused.'
- Responses changed
  - New response: 409

GET /api/admin/matrix-appservice/status/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: tokens_managed_by
          - Properties changed
            - New property: tokens_managed_by

GET /api/admin/matrix/diagnostics/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checks
              - Items changed
                - Properties changed
                  - New property: metrics

GET /api/admin/matrix/livekit/participants/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: tracks
                - Items changed
                  - Required changed
                    - New required property: encryption
                    - New required property: source
                  - Properties changed
                    - New property: encryption
                    - New property: source

POST /api/admin/matrix/reprovision/

- Description changed from 'Resets all active rooms to 'creating' state and re-queues them for provisioning. Also resets all user profiles. Staff only.' to 'Resets all active rooms to 'creating' state and re-queues them for provisioning. Also resets all user profiles. Only for moving to a new homeserver: on the same homeserver, every old room stays behind with its history next to a new, empty one. Staff only.'

GET /api/anonymous-chat-interactions/conversations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: max_severity_rank
            - Properties changed
              - New property: max_severity_rank

GET /api/anonymous-chat-interactions/kpi/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: clarification_rate
            - New required property: clarification_requests_total
          - Properties changed
            - New property: clarification_rate
            - New property: clarification_requests_total

GET /api/autoprovisioning-rules/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: customer_role_description
              - New required property: customer_role_display_name
            - Properties changed
              - New property: create_project
              - New property: customer_role
              - New property: customer_role_description
              - New property: customer_role_display_name
              - New property: project_name_template
              - New property: revoke_when_unmatched
              - New property: user_assurance_levels
              - New property: user_claims
              - New property: user_identity_sources
              - New property: user_nationalities
              - New property: user_organization_types

POST /api/autoprovisioning-rules/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: create_project
          - New property: customer_role
          - New property: customer_role_name
          - New property: project_name_template
          - New property: revoke_when_unmatched
          - New property: user_assurance_levels
          - New property: user_claims
          - New property: user_identity_sources
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_role_description
            - New required property: customer_role_display_name
          - Properties changed
            - New property: create_project
            - New property: customer_role
            - New property: customer_role_description
            - New property: customer_role_display_name
            - New property: project_name_template
            - New property: revoke_when_unmatched
            - New property: user_assurance_levels
            - New property: user_claims
            - New property: user_identity_sources
            - New property: user_nationalities
            - New property: user_organization_types

GET /api/autoprovisioning-rules/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_role_description
            - New required property: customer_role_display_name
          - Properties changed
            - New property: create_project
            - New property: customer_role
            - New property: customer_role_description
            - New property: customer_role_display_name
            - New property: project_name_template
            - New property: revoke_when_unmatched
            - New property: user_assurance_levels
            - New property: user_claims
            - New property: user_identity_sources
            - New property: user_nationalities
            - New property: user_organization_types

PATCH /api/autoprovisioning-rules/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: create_project
          - New property: customer_role
          - New property: customer_role_name
          - New property: project_name_template
          - New property: revoke_when_unmatched
          - New property: user_assurance_levels
          - New property: user_claims
          - New property: user_identity_sources
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_role_description
            - New required property: customer_role_display_name
          - Properties changed
            - New property: create_project
            - New property: customer_role
            - New property: customer_role_description
            - New property: customer_role_display_name
            - New property: project_name_template
            - New property: revoke_when_unmatched
            - New property: user_assurance_levels
            - New property: user_claims
            - New property: user_identity_sources
            - New property: user_nationalities
            - New property: user_organization_types

PUT /api/autoprovisioning-rules/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: create_project
          - New property: customer_role
          - New property: customer_role_name
          - New property: project_name_template
          - New property: revoke_when_unmatched
          - New property: user_assurance_levels
          - New property: user_claims
          - New property: user_identity_sources
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_role_description
            - New required property: customer_role_display_name
          - Properties changed
            - New property: create_project
            - New property: customer_role
            - New property: customer_role_description
            - New property: customer_role_display_name
            - New property: project_name_template
            - New property: revoke_when_unmatched
            - New property: user_assurance_levels
            - New property: user_claims
            - New property: user_identity_sources
            - New property: user_nationalities
            - New property: user_organization_types

POST /api/autoprovisioning-rules/{uuid}/test-match/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: project_action
            - New required property: unconfigured_claims
            - New required property: user_claims
          - Properties changed
            - New property: project_action
            - New property: unconfigured_claims
            - New property: user_claims

GET /api/backend-resources/

- Extensions changed
  - Deleted extension: x-permissions

HEAD /api/backend-resources/

- Extensions changed
  - Deleted extension: x-permissions

POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_account_settings
            - New property: project_start_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
            - Modified property: is_limit_based
              - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
            - Modified property: is_usage_based
              - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_settings billing_mode_components billing_period_applies can_update_integration can_update_options compliance_checklist_details scope_resource scope_resource_name scope_resource_uuid user_has_offering_user]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: account_settings
              - New property: billing_mode_components
              - New property: billing_period_applies
              - New property: can_update_integration
              - New property: can_update_options
              - New property: compliance_checklist_details
              - New property: scope_resource
              - New property: scope_resource_name
              - New property: scope_resource_uuid
              - New property: user_has_offering_user
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: component_formula_config
                            - New property: component_sum_config
                            - New property: pattern
                            - New property: pattern_error
                            - New property: unique
                            - New property: visible_if
                            - Modified property: default_configs
                              - Properties changed
                                - New property: load_balancer_mode
                                - New property: topology_mode
                            - Modified property: type
                              - New enum values: [component_formula component_sum]
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: account_scope
                      - New property: enable_api_key_provisioning
                      - New property: enable_resource_limit_change_requests
                      - New property: enable_scim_entitlements
                      - New property: heappe_identifier
                      - New property: hide_api_keys_tab
                      - New property: scim_login_nodes
                      - New property: uses_robot_accounts
                      - Modified property: disable_autoapprove
                        - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                      - Modified property: heappe_cluster_id
                        - Nullable changed from false to true
                      - Modified property: heappe_local_base_path
                        - Nullable changed from false to true
                      - Modified property: heappe_url
                        - Nullable changed from false to true
                      - Modified property: heappe_username
                        - Nullable changed from false to true
                      - Modified property: homedir_prefix
                        - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                        - Default changed from '/home/' to null
                      - Modified property: login_shell
                        - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                        - Default changed from '/bin/bash' to null
                      - Modified property: project_permanent_directory
                        - Nullable changed from false to true
                      - Modified property: scratch_project_directory
                        - Nullable changed from false to true
                      - Modified property: username_anonymized_prefix
                        - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                        - Default changed from 'waldur_' to null
                      - Modified property: username_generation_policy
                        - Property 'OneOf' changed
                          - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                        - Property 'AllOf' changed
                          - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                        - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                        - Default changed from 'service_provider' to null
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: component_formula_config
                            - New property: component_sum_config
                            - New property: pattern
                            - New property: pattern_error
                            - New property: unique
                            - New property: visible_if
                            - Modified property: default_configs
                              - Properties changed
                                - New property: load_balancer_mode
                                - New property: topology_mode
                            - Modified property: type
                              - New enum values: [component_formula component_sum]
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: catalog
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/CatalogSummary
                          - Properties changed
                            - New property: supports_cpu_target_restrictions

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_settings billing_mode_components billing_period_applies can_update_integration can_update_options compliance_checklist_details scope_resource scope_resource_name scope_resource_uuid user_has_offering_user]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_settings
            - New property: billing_mode_components
            - New property: billing_period_applies
            - New property: can_update_integration
            - New property: can_update_options
            - New property: compliance_checklist_details
            - New property: scope_resource
            - New property: scope_resource_name
            - New property: scope_resource_uuid
            - New property: user_has_offering_user
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: billing_mode
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: billing_type
                        - New property: is_prepaid
                        - New property: limit_period
                        - Modified property: measured_unit
                          - Description changed from 'Unit of measurement, for example, GB.' to ''
                          - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/CatalogSummary
                        - Properties changed
                          - New property: supports_cpu_target_restrictions

GET /api/booking-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_account_settings project_start_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_account_settings
              - New property: project_start_date
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: new_plan_billing_mode
                      - New property: old_plan_billing_mode
                      - New property: resource_end_date
                      - Modified property: limits
                        - AdditionalProperties changed
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                      - Modified property: old_cost_estimate
                        - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
              - Modified property: is_limit_based
                - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
              - Modified property: is_usage_based
                - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
              - Modified property: limits
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: new_plan_billing_mode
                      - New property: old_plan_billing_mode
                      - New property: resource_end_date
                      - Modified property: limits
                        - AdditionalProperties changed
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                      - Modified property: old_cost_estimate
                        - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_account_settings project_start_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_account_settings
            - New property: project_start_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
            - Modified property: is_limit_based
              - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
            - Modified property: is_usage_based
              - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/call-managing-organisations/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source

HEAD /api/call-managing-organisations/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

GET /api/call-reviewer-pools/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: current_assignments
                - Description changed from '' to 'Number of the reviewer's open assignments in this call: pending or accepted assignment items whose review is not finished, plus reviews in progress created without an assignment item.'

GET /api/call-reviewer-pools/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_assignments
              - Description changed from '' to 'Number of the reviewer's open assignments in this call: pending or accepted assignment items whose review is not finished, plus reviews in progress created without an assignment item.'

POST /api/call-reviewer-pools/{uuid}/force-accept/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_assignments
              - Description changed from '' to 'Number of the reviewer's open assignments in this call: pending or accepted assignment items whose review is not finished, plus reviews in progress created without an assignment item.'

GET /api/conflicts-of-interest/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: status
            - Properties changed
              - Modified property: status
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/ConflictOfInterestStatusEnum
                - Type changed from 'string' to ''
                - Deleted enum values: [pending dismissed waived recused]
                - ReadOnly changed from false to true

GET /api/conflicts-of-interest/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ConflictOfInterestStatusEnum
              - Type changed from 'string' to ''
              - Deleted enum values: [pending dismissed waived recused]
              - ReadOnly changed from false to true

PATCH /api/conflicts-of-interest/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: status
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ConflictOfInterestStatusEnum
              - Type changed from 'string' to ''
              - Deleted enum values: [pending dismissed waived recused]
              - ReadOnly changed from false to true

PUT /api/conflicts-of-interest/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: status
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ConflictOfInterestStatusEnum
              - Type changed from 'string' to ''
              - Deleted enum values: [pending dismissed waived recused]
              - ReadOnly changed from false to true

POST /api/conflicts-of-interest/{uuid}/dismiss/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ConflictOfInterestStatusEnum
              - Type changed from 'string' to ''
              - Deleted enum values: [pending dismissed waived recused]
              - ReadOnly changed from false to true

POST /api/conflicts-of-interest/{uuid}/recuse/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ConflictOfInterestStatusEnum
              - Type changed from 'string' to ''
              - Deleted enum values: [pending dismissed waived recused]
              - ReadOnly changed from false to true

POST /api/conflicts-of-interest/{uuid}/waive/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ConflictOfInterestStatusEnum
              - Type changed from 'string' to ''
              - Deleted enum values: [pending dismissed waived recused]
              - ReadOnly changed from false to true

GET /api/credit-transactions/

- New query param: billing_period
- New query param: billing_period_after
- New query param: billing_period_before
- New query param: project_credit_uuid
- New query param: project_uuid
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-billing_period billing_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: billing_period
              - New property: project_name
              - New property: project_uuid
              - Modified property: customer_name
                - Nullable changed from false to true
              - Modified property: customer_uuid
                - Nullable changed from false to true
              - Modified property: transaction_type
                - New enum values: [minimal_draw]

HEAD /api/credit-transactions/

- New query param: billing_period
- New query param: billing_period_after
- New query param: billing_period_before
- New query param: project_credit_uuid
- New query param: project_uuid
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-billing_period billing_period]

GET /api/credit-transactions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_period
            - New property: project_name
            - New property: project_uuid
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: transaction_type
              - New enum values: [minimal_draw]

POST /api/customer-credits/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: offerings
            - Description changed from '' to 'Offerings the credit may be drawn against. Leave empty to allow all offerings: an empty list means unrestricted, not none. Cost on any other offering is invoiced normally and is never compensated from this credit.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Description changed from '' to 'Offerings the credit may be drawn against. Leave empty to allow all offerings: an empty list means unrestricted, not none. Cost on any other offering is invoiced normally and is never compensated from this credit.'

PATCH /api/customer-credits/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: offerings
            - Description changed from '' to 'Offerings the credit may be drawn against. Leave empty to allow all offerings: an empty list means unrestricted, not none. Cost on any other offering is invoiced normally and is never compensated from this credit.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Description changed from '' to 'Offerings the credit may be drawn against. Leave empty to allow all offerings: an empty list means unrestricted, not none. Cost on any other offering is invoiced normally and is never compensated from this credit.'

PUT /api/customer-credits/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: offerings
            - Description changed from '' to 'Offerings the credit may be drawn against. Leave empty to allow all offerings: an empty list means unrestricted, not none. Cost on any other offering is invoiced normally and is never compensated from this credit.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Description changed from '' to 'Offerings the credit may be drawn against. Leave empty to allow all offerings: an empty list means unrestricted, not none. Cost on any other offering is invoiced normally and is never compensated from this credit.'

GET /api/customer-quotas/

- New query param: customer_uuid

HEAD /api/customer-quotas/

- New query param: customer_uuid

GET /api/customers/

- Description changed from 'Retrieve a list of customers. The list is filtered based on the user's permissions.' to 'Retrieve a list of customers. The list is filtered based on the user's permissions. A user whose only link to an organization is a role on its service provider sees it with a restricted field set: url, uuid, name, native_name, display_name, abbreviation, slug, image, country, country_name, is_service_provider, service_provider and service_provider_uuid. All other fields are omitted for that row.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_service_provider_manager_only]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: is_service_provider_manager_only

POST /api/customers/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_service_provider_manager_only

GET /api/customers/{customer_uuid}/project-metadata-question-answers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_answers
                - Description changed from 'Get all project answers for this question.' to ''
                - Items changed
                  - Required changed
                    - New required property: answer_data
                    - New required property: answer_uuid
                    - New required property: answered_at
                    - New required property: answered_by
                    - New required property: project_name
                    - New required property: project_uuid
                    - New required property: requires_review
                  - Properties changed
                    - New property: answer_data
                    - New property: answer_uuid
                    - New property: answered_at
                    - New property: answered_by
                    - New property: project_name
                    - New property: project_uuid
                    - New property: requires_review
                  - AdditionalProperties changed
                    - Schema deleted

GET /api/customers/{uuid}/

- Description changed from 'Fetch the details of a specific customer by its UUID.' to 'Fetch the details of a specific customer by its UUID. A user whose only link to the organization is a role on its service provider receives the restricted field set described on the list operation.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_service_provider_manager_only]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_service_provider_manager_only

PATCH /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_service_provider_manager_only

PUT /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_service_provider_manager_only

GET /api/customers/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source

HEAD /api/customers/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

GET /api/customers/{uuid}/stats/

- New query param: include_terminated
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Required changed
                  - New required property: limit_usage_terminated
                  - New required property: usage_terminated
                - Properties changed
                  - New property: limit_usage_terminated
                  - New property: usage_terminated

GET /api/event-consumers/

- New query param: is_global
- New query param: o
- New query param: user_username
- New query param: user_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: auth_kind
              - New required property: auth_token_name
              - New required property: auth_token_prefix
              - New required property: authorized_via
              - New required property: delivery_blocked_reason
              - New required property: user_full_name
              - New required property: user_is_staff
              - New required property: user_username
              - New required property: user_uuid
            - Properties changed
              - New property: auth_kind
              - New property: auth_token_name
              - New property: auth_token_prefix
              - New property: authorized_via
              - New property: delivery_blocked_reason
              - New property: user_full_name
              - New property: user_is_staff
              - New property: user_username
              - New property: user_uuid
              - Modified property: object_types
                - Type changed from 'object' to 'array'
                - Description changed from 'List of observable object types this consumer receives. Empty list means all types.' to ''
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added

HEAD /api/event-consumers/

- New query param: is_global
- New query param: o
- New query param: user_username
- New query param: user_uuid

POST /api/event-consumers/register/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: object_types
            - Items changed
              - New enum values: [service_provider_account service_provider_project_group call proposal]

POST /api/event-subscriptions/{uuid}/create_queue/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: object_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ObservableObjectTypeEnum
                - New enum values: [service_provider_account service_provider_project_group call proposal]

GET /api/events/event_groups/

- Description changed from 'Returns a list of groups with event types.
Group is used in exclude_features query param.' to 'Returns a list of groups with event types.
Group is used in exclude_features query param.

Narrowed to the groups this deployment can emit. Groups left out stay
deliverable and writable -- see waldur_core.logging.availability.'

GET /api/google-auth/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_options]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: account_options

GET /api/google-auth/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_options]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_options

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
                  - New enum values: [openstack_resources]
              - Modified property: event_types
                - Items changed
                  - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_resources]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_resources]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_resources]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_resources]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_resources]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_resources]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_resources]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

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
                  - New enum values: [openstack_resources]
              - Modified property: event_types
                - Items changed
                  - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_resources]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_resources]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_resources]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_resources]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_resources]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_resources]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_resources]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

POST /api/identity-bridge/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: organization_address
          - New property: organization_registry_code
          - New property: organization_vat_code
          - New property: primary_gid
          - New property: uid_number

GET /api/invoices/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: items
                - Items changed
                  - Properties changed
                    - Modified property: details
                      - Properties changed
                        - Modified property: resource_limit_periods
                          - Items changed
                            - Properties changed
                              - Modified property: quantity
                                - Type changed from 'integer' to 'number'
                                - Format changed from '' to 'double'

GET /api/invoices/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: items
              - Items changed
                - Properties changed
                  - Modified property: details
                    - Properties changed
                      - Modified property: resource_limit_periods
                        - Items changed
                          - Properties changed
                            - Modified property: quantity
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'

GET /api/invoices/{uuid}/items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: details
              - Properties changed
                - Modified property: resource_limit_periods
                  - Items changed
                    - Properties changed
                      - Modified property: quantity
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'

GET /api/managed-rancher-cluster-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_account_settings project_start_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_account_settings
              - New property: project_start_date
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: new_plan_billing_mode
                      - New property: old_plan_billing_mode
                      - New property: resource_end_date
                      - Modified property: limits
                        - AdditionalProperties changed
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                      - Modified property: old_cost_estimate
                        - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
              - Modified property: is_limit_based
                - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
              - Modified property: is_usage_based
                - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
              - Modified property: limits
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: new_plan_billing_mode
                      - New property: old_plan_billing_mode
                      - New property: resource_end_date
                      - Modified property: limits
                        - AdditionalProperties changed
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                      - Modified property: old_cost_estimate
                        - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/managed-rancher-cluster-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_account_settings project_start_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_account_settings
            - New property: project_start_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
            - Modified property: is_limit_based
              - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
            - Modified property: is_usage_based
              - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/marketplace-component-usages/

- New query param: missing_usage_policy
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [missing_usage_policy]
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-missing_usage_policy missing_usage_policy]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: missing_usage_policy
              - Modified property: recurring
                - Description changed from 'Reported value is reused every month until changed.' to 'Deprecated, use missing_usage_policy instead. True when the reported value is reused every month until changed.'
                - ReadOnly changed from false to true

HEAD /api/marketplace-component-usages/

- New query param: missing_usage_policy
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-missing_usage_policy missing_usage_policy]

POST /api/marketplace-component-usages/set_usage/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: usages
            - Items changed
              - Properties changed
                - New property: missing_usage_policy
                - Modified property: recurring
                  - Description changed from 'Whether this usage is recurring' to 'Deprecated, use missing_usage_policy instead. True is equivalent to missing_usage_policy='reuse'.'
                  - Default changed from false to null
                  - Nullable changed from false to true
      - Examples changed
        - Modified example: ReportUsageForMultipleComponents
          - Value changed from map[plan_period:a1b2c3d4-e5f6-7890-1234-567890abcdef usages:[map[amount:120.5 description:CPU usage for the last period type:cpu] map[amount:240 description:RAM usage for the last period recurring:true type:ram]]] to map[plan_period:a1b2c3d4-e5f6-7890-1234-567890abcdef usages:[map[amount:120.5 description:CPU usage for the last period type:cpu] map[amount:240 description:RAM usage for the last period missing_usage_policy:reuse type:ram]]]

GET /api/marketplace-component-usages/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [missing_usage_policy]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: missing_usage_policy
            - Modified property: recurring
              - Description changed from 'Reported value is reused every month until changed.' to 'Deprecated, use missing_usage_policy instead. True when the reported value is reused every month until changed.'
              - ReadOnly changed from false to true

POST /api/marketplace-component-usages/{uuid}/set_user_usage/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'resource.offering.customer.serviceprovider'

POST /api/marketplace-component-usages/{uuid}/set_user_usages/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'resource.offering.customer.serviceprovider'

GET /api/marketplace-course-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: user_uuid
                - Nullable changed from false to true
              - Modified property: username
                - Nullable changed from false to true

POST /api/marketplace-course-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_uuid
              - Nullable changed from false to true
            - Modified property: username
              - Nullable changed from false to true

POST /api/marketplace-course-accounts/create_bulk/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: user_uuid
                - Nullable changed from false to true
              - Modified property: username
                - Nullable changed from false to true

DELETE /api/marketplace-course-accounts/{uuid}/

- Responses changed
  - New response: 202
  - Deleted response: 204

GET /api/marketplace-course-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_uuid
              - Nullable changed from false to true
            - Modified property: username
              - Nullable changed from false to true

POST /api/marketplace-course-accounts/{uuid}/retry/

- Responses changed
  - Modified response: 202
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_uuid
              - Nullable changed from false to true
            - Modified property: username
              - Nullable changed from false to true

GET /api/marketplace-customer-estimated-cost-policies/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
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
              - New property: current_cost
              - New property: eta_date
              - New property: eta_days

POST /api/marketplace-customer-estimated-cost-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

GET /api/marketplace-customer-estimated-cost-policies/{uuid}/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

PATCH /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

PUT /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

GET /api/marketplace-customer-usage/{uuid}/components-usage-by-project/

- New query param: include_terminated
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: projects
              - Items changed
                - Required changed
                  - New required property: is_removed
                  - New required property: usage_terminated
                - Properties changed
                  - New property: is_removed
                  - New property: usage_terminated
                  - Modified property: buckets
                    - Items changed
                      - Required changed
                        - New required property: usage_terminated
                      - Properties changed
                        - New property: usage_terminated

GET /api/marketplace-customer-usage/{uuid}/components-usage-timeseries/

- New query param: include_terminated
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: buckets
              - Items changed
                - Required changed
                  - New required property: usage_terminated
                - Properties changed
                  - New property: usage_terminated

GET /api/marketplace-customer-usage/{uuid}/components-usage/

- Description changed from 'Returns one row per (offering, component type, billing type) for all non-terminated resources within the scope. Each row's `usage` and `limit_usage` are aggregated using the offering's own `limit_period`.' to 'Returns one row per (offering, component type, billing type) for all non-terminated resources within the scope (or all resources when `include_terminated` is true). Each row's `usage` and `limit_usage` are aggregated using the offering's own `limit_period`.'
- New query param: include_terminated
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Required changed
                  - New required property: limit_usage_terminated
                  - New required property: usage_terminated
                - Properties changed
                  - New property: limit_usage_terminated
                  - New property: usage_terminated

GET /api/marketplace-offering-estimated-cost-policies/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
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
              - New property: current_cost
              - New property: eta_date
              - New property: eta_days

POST /api/marketplace-offering-estimated-cost-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

GET /api/marketplace-offering-estimated-cost-policies/{uuid}/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

PATCH /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

PUT /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

GET /api/marketplace-offering-users/

- New query param: is_provider_backed
- New query param: service_provider_account_uuid
- New query param: username
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_provider_account_username service_provider_account_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: service_provider_account_username
              - New property: service_provider_account_uuid

HEAD /api/marketplace-offering-users/

- New query param: is_provider_backed
- New query param: service_provider_account_uuid
- New query param: username

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_account_username
            - New property: service_provider_account_uuid

GET /api/marketplace-offering-users/posix_identities/

- Description changed from 'Consolidated view of one user's POSIX identifiers (UID, primary GID and project group GIDs) across every offering they have an account on, each with the range it was allocated from. Scoped to the offering users the requester is allowed to see.' to 'Consolidated view of one user's POSIX identifiers (UID, primary GID and project group GIDs), one row per pool and namespace: a UID allocated once for the user is reported once, listing every offering that uses it. An offering with its own pool yields its own row. Scoped to the offering users the requester is allowed to see.'
- New query param: is_provider_backed
- New query param: service_provider_account_uuid
- New query param: username
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: offerings
              - New required property: pool_scope
            - Properties changed
              - New property: offerings
              - New property: pool_scope
              - Modified property: offering_name
                - Description changed from '' to 'Deprecated: the first entry of 'offerings'. The endpoint used to return one row per offering; read 'offerings' instead.'
                - Nullable changed from false to true
              - Modified property: offering_uuid
                - Description changed from '' to 'Deprecated: the first entry of 'offerings'. Read 'offerings' instead.'
                - Nullable changed from false to true

HEAD /api/marketplace-offering-users/posix_identities/

- New query param: is_provider_backed
- New query param: service_provider_account_uuid
- New query param: username

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_provider_account_username service_provider_account_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_account_username
            - New property: service_provider_account_uuid

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_account_username
            - New property: service_provider_account_uuid

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_account_username
            - New property: service_provider_account_uuid

GET /api/marketplace-offering-users/{uuid}/posix_allocations/

- Description changed from 'Returns the user's POSIX identifiers (UID, primary GID) and, for each, the POSIX ID pool that tracks it. The pool fields are null when the value is not tracked by a pool.' to 'Returns the user's POSIX identifiers (UID, primary GID) and, for each, the POSIX ID pool that tracks it plus the user's other offerings that resolve to the same pool and therefore carry the very same value. The pool fields are null when the value is not tracked by a pool.'
- New query param: is_provider_backed
- New query param: service_provider_account_uuid
- New query param: username
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: shared_with_offerings
            - Properties changed
              - New property: shared_with_offerings

GET /api/marketplace-offering-users/{uuid}/posix_groups/

- New query param: is_provider_backed
- New query param: service_provider_account_uuid
- New query param: username
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: group_name
              - New required property: kind
              - New required property: pool_scope
              - New required property: service_provider_name
            - Properties changed
              - New property: group_name
              - New property: kind
              - New property: pool_scope
              - New property: service_provider_name

POST /api/marketplace-offering-users/{uuid}/set_error_creating/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-users/{uuid}/set_error_deleting/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-users/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Manually sets the offering user state to 'OK'. This can be used to recover from an error state or to complete a manual creation process.' to 'Manually sets the offering user state to 'OK'. This can be used to recover from an error state or to complete a manual creation process. This clears any service provider comments.'

POST /api/marketplace-offering-users/{uuid}/set_posix_attributes/

- Description changed from 'Override the login shell, home directory, UID and/or primary GID for a single offering user, taking precedence over the offering-level defaults / the range allocator. This is the programmatic equivalent of the 'Edit POSIX attributes' dialog. The accepted fields are 'login_shell', 'home_directory', 'uidnumber' and 'primarygroup'; all are optional, but at least one must be provided.

A UID or primary GID re-points the allocation ledger and must fall within the POSIX ID pool resolved for the offering: a value outside that pool's range is rejected with 400, as is a value already held by another active identity (another account, a robot account or a group) and any override on an offering for which no pool resolves. The action is all-or-nothing - a conflict on the second identifier rolls back the change made for the first.

The response 'warnings' list carries only non-fatal advisories about values that were accepted: the reserved POSIX ids 65534 and 65535, and values of 2^31 or above, which may break software using signed 32-bit ids.' to 'Override the login shell, home directory, UID and/or primary GID for a single offering user, taking precedence over the offering-level defaults / the range allocator. This is the programmatic equivalent of the 'Edit POSIX attributes' dialog. The accepted fields are 'login_shell', 'home_directory', 'uidnumber' and 'primarygroup'; all are optional, but at least one must be provided.

A UID or primary GID re-points the allocation ledger and must fall within the POSIX ID pool resolved for the offering: a value outside that pool's range is rejected with 400, as is a value already held by another active identity (another account, a robot account or a group) and any override on an offering for which no pool resolves. The action is all-or-nothing - a conflict on the second identifier rolls back the change made for the first.

A UID or primary GID belongs to the user within the pool, not to this single account, so the pin applies across every offering of the provider that resolves to the same pool. An offering with its own pool is unaffected.

The response 'warnings' list carries only non-fatal advisories about values that were accepted: the reserved POSIX ids 65534 and 65535, and values of 2^31 or above, which may break software using signed 32-bit ids.'

GET /api/marketplace-openstack-duplicate-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: blockers
              - New required property: duplicate_uuids
              - New required property: keeper_uuid
              - New required property: suggested_mapping
              - New required property: warnings
            - Properties changed
              - New property: blockers
              - New property: duplicate_uuids
              - New property: keeper_uuid
              - New property: suggested_mapping
              - New property: warnings

GET /api/marketplace-orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [new_plan_billing_mode old_plan_billing_mode resource_end_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: new_plan_billing_mode
              - New property: old_plan_billing_mode
              - New property: resource_end_date
              - Modified property: limits
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: old_cost_estimate
                - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Property 'OneOf' changed
              - Schemas deleted: #/components/schemas/AzureVirtualMachineCreateOrderAttributes, #/components/schemas/AzureSQLServerCreateOrderAttributes, #/components/schemas/SlurmInvoicesSlurmPackageCreateOrderAttributes
              - Modified schema: #/components/schemas/OpenStackInstanceCreateOrderAttributes
                - Properties changed
                  - New property: metadata
              - Modified schema: #/components/schemas/VMwareVirtualMachineCreateOrderAttributes
                - Properties changed
                  - New property: folder
                  - New property: networks
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'Slug of the new resource. Used when the caller is staff or holds RESOURCE.SET_SLUG on the project, the offering or their organizations; otherwise ignored.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: new_plan_billing_mode
            - New property: old_plan_billing_mode
            - New property: resource_end_date
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: old_cost_estimate
              - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [new_plan_billing_mode old_plan_billing_mode resource_end_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: new_plan_billing_mode
            - New property: old_plan_billing_mode
            - New property: resource_end_date
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: old_cost_estimate
              - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

PATCH /api/marketplace-orders/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'

PUT /api/marketplace-orders/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'

POST /api/marketplace-orders/{uuid}/approve_by_provider/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'
    - Added /0/scopes/- with value: 'offering.customer.serviceprovider'
- Responses changed
  - New response: 409

GET /api/marketplace-orders/{uuid}/offering/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_settings billing_mode_components billing_period_applies can_update_integration can_update_options compliance_checklist_details scope_resource scope_resource_name scope_resource_uuid user_has_offering_user]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_settings
            - New property: billing_mode_components
            - New property: billing_period_applies
            - New property: can_update_integration
            - New property: can_update_options
            - New property: compliance_checklist_details
            - New property: scope_resource
            - New property: scope_resource_name
            - New property: scope_resource_uuid
            - New property: user_has_offering_user
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: billing_mode
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: billing_type
                        - New property: is_prepaid
                        - New property: limit_period
                        - Modified property: measured_unit
                          - Description changed from 'Unit of measurement, for example, GB.' to ''
                          - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/CatalogSummary
                        - Properties changed
                          - New property: supports_cpu_target_restrictions

POST /api/marketplace-orders/{uuid}/reject_by_provider/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'
    - Added /0/scopes/- with value: 'offering.customer.serviceprovider'
- Responses changed
  - New response: 409

GET /api/marketplace-orders/{uuid}/resource/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_account_settings project_start_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_account_settings
            - New property: project_start_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
            - Modified property: is_limit_based
              - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
            - Modified property: is_usage_based
              - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

POST /api/marketplace-orders/{uuid}/retry/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Modified /0/scopes/1 from 'offering' to 'offering.customer'
    - Added /0/scopes/- with value: 'offering.customer.serviceprovider'

POST /api/marketplace-orders/{uuid}/set_backend_id/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering.customer.serviceprovider'

POST /api/marketplace-orders/{uuid}/set_provider_info/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'
    - Added /0/scopes/- with value: 'offering.customer.serviceprovider'

POST /api/marketplace-orders/{uuid}/set_state_done/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Modified /0/scopes/1 from 'offering' to 'offering.customer'
    - Added /0/scopes/- with value: 'offering.customer.serviceprovider'

POST /api/marketplace-orders/{uuid}/set_state_erred/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Modified /0/scopes/1 from 'offering.customer.serviceprovider' to 'offering.customer'
    - Modified /0/scopes/2 from 'offering' to 'offering.customer.serviceprovider'

POST /api/marketplace-orders/{uuid}/set_state_executing/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Modified /0/scopes/1 from 'offering' to 'offering.customer'
    - Added /0/scopes/- with value: 'offering.customer.serviceprovider'

GET /api/marketplace-plan-components/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: measured_unit
                - Description changed from 'Unit of measurement, for example, GB.' to ''
                - Nullable changed from false to true

GET /api/marketplace-plan-components/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: measured_unit
              - Description changed from 'Unit of measurement, for example, GB.' to ''
              - Nullable changed from false to true

GET /api/marketplace-plans/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: billing_mode
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: billing_type
                    - New property: is_prepaid
                    - New property: limit_period
                    - Modified property: measured_unit
                      - Description changed from 'Unit of measurement, for example, GB.' to ''
                      - Nullable changed from false to true

POST /api/marketplace-plans/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: billing_mode
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_mode
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: billing_type
                  - New property: is_prepaid
                  - New property: limit_period
                  - Modified property: measured_unit
                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                    - Nullable changed from false to true

GET /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_mode
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: billing_type
                  - New property: is_prepaid
                  - New property: limit_period
                  - Modified property: measured_unit
                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                    - Nullable changed from false to true

PATCH /api/marketplace-plans/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: billing_mode
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_mode
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: billing_type
                  - New property: is_prepaid
                  - New property: limit_period
                  - Modified property: measured_unit
                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                    - Nullable changed from false to true

PUT /api/marketplace-plans/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: billing_mode
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_mode
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: billing_type
                  - New property: is_prepaid
                  - New property: limit_period
                  - Modified property: measured_unit
                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                    - Nullable changed from false to true

GET /api/marketplace-posix-id-pools/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [group_gid_used group_gid_utilization max_group_gid min_group_gid next_group_gid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: group_gid_used
              - New property: group_gid_utilization
              - New property: max_group_gid
              - New property: min_group_gid
              - New property: next_group_gid

POST /api/marketplace-posix-id-pools/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: max_group_gid
          - New property: min_group_gid
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: group_gid_used
            - New property: group_gid_utilization
            - New property: max_group_gid
            - New property: min_group_gid
            - New property: next_group_gid

GET /api/marketplace-posix-id-pools/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [group_gid_used group_gid_utilization max_group_gid min_group_gid next_group_gid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: group_gid_used
            - New property: group_gid_utilization
            - New property: max_group_gid
            - New property: min_group_gid
            - New property: next_group_gid

PATCH /api/marketplace-posix-id-pools/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: max_group_gid
          - New property: min_group_gid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: group_gid_used
            - New property: group_gid_utilization
            - New property: max_group_gid
            - New property: min_group_gid
            - New property: next_group_gid

PUT /api/marketplace-posix-id-pools/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: max_group_gid
          - New property: min_group_gid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: group_gid_used
            - New property: group_gid_utilization
            - New property: max_group_gid
            - New property: min_group_gid
            - New property: next_group_gid

GET /api/marketplace-posix-id-pools/{uuid}/stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: group_gid
          - Properties changed
            - New property: group_gid

GET /api/marketplace-posix-identities/

- New query param: consumer_type
- New query param: gid
- New query param: gid_max
- New query param: gid_min
- New query param: keyword
- New query param: o
- New query param: recyclable
- New query param: uid
- New query param: uid_max
- New query param: uid_min
- New query param: user_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: user_username
              - New required property: user_uuid
            - Properties changed
              - New property: recyclable
              - New property: user_username
              - New property: user_uuid
              - Modified property: offering_name
                - Nullable changed from false to true
              - Modified property: offering_uuid
                - Nullable changed from false to true

HEAD /api/marketplace-posix-identities/

- New query param: consumer_type
- New query param: gid
- New query param: gid_max
- New query param: gid_min
- New query param: keyword
- New query param: o
- New query param: recyclable
- New query param: uid
- New query param: uid_max
- New query param: uid_min
- New query param: user_uuid

GET /api/marketplace-posix-identities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: user_username
            - New required property: user_uuid
          - Properties changed
            - New property: recyclable
            - New property: user_username
            - New property: user_uuid
            - Modified property: offering_name
              - Nullable changed from false to true
            - Modified property: offering_uuid
              - Nullable changed from false to true

GET /api/marketplace-project-estimated-cost-policies/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
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
              - Deleted required property: resource_name
              - Deleted required property: scope
              - Deleted required property: scope_name
              - Deleted required property: scope_uuid
              - Deleted required property: url
              - Deleted required property: uuid
            - Properties changed
              - New property: current_cost
              - New property: eta_date
              - New property: eta_days

POST /api/marketplace-project-estimated-cost-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - Deleted required property: resource_name
            - Deleted required property: scope
            - Deleted required property: scope_name
            - Deleted required property: scope_uuid
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

GET /api/marketplace-project-estimated-cost-policies/{uuid}/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - Deleted required property: resource_name
            - Deleted required property: scope
            - Deleted required property: scope_name
            - Deleted required property: scope_uuid
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

PATCH /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - Deleted required property: resource_name
            - Deleted required property: scope
            - Deleted required property: scope_name
            - Deleted required property: scope_uuid
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

PUT /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
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
            - Deleted required property: resource_name
            - Deleted required property: scope
            - Deleted required property: scope_name
            - Deleted required property: scope_uuid
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: current_cost
            - New property: eta_date
            - New property: eta_days

GET /api/marketplace-project-posix-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: group_name
              - New property: group_uuid
              - New property: in_use
              - New property: member_count
              - New property: members
              - New property: offerings
              - New property: service_provider_uuid
              - Modified property: gid
                - Nullable changed from false to true
              - Modified property: kind
                - New enum values: [provider_project_group]
              - Modified property: offering_name
                - Nullable changed from false to true
              - Modified property: offering_uuid
                - Nullable changed from false to true

GET /api/marketplace-project-usage/{uuid}/components-usage-timeseries/

- New query param: include_terminated
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: buckets
              - Items changed
                - Required changed
                  - New required property: usage_terminated
                - Properties changed
                  - New property: usage_terminated

GET /api/marketplace-project-usage/{uuid}/components-usage/

- Description changed from 'Returns one row per (offering, component type, billing type) for all non-terminated resources within the scope. Each row's `usage` and `limit_usage` are aggregated using the offering's own `limit_period`.' to 'Returns one row per (offering, component type, billing type) for all non-terminated resources within the scope (or all resources when `include_terminated` is true). Each row's `usage` and `limit_usage` are aggregated using the offering's own `limit_period`.'
- New query param: include_terminated
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Required changed
                  - New required property: limit_usage_terminated
                  - New required property: usage_terminated
                - Properties changed
                  - New property: limit_usage_terminated
                  - New property: usage_terminated

GET /api/marketplace-provider-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_settings billing_mode_components billing_period_applies can_update_integration can_update_options compliance_checklist_details limit_precision_advisory scope_resource scope_resource_name scope_resource_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: account_settings
              - New property: billing_mode_components
              - New property: billing_period_applies
              - New property: can_update_integration
              - New property: can_update_options
              - New property: compliance_checklist_details
              - New property: limit_precision_advisory
              - New property: scope_resource
              - New property: scope_resource_name
              - New property: scope_resource_uuid
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: component_formula_config
                            - New property: component_sum_config
                            - New property: pattern
                            - New property: pattern_error
                            - New property: unique
                            - New property: visible_if
                            - Modified property: default_configs
                              - Properties changed
                                - New property: load_balancer_mode
                                - New property: topology_mode
                            - Modified property: type
                              - New enum values: [component_formula component_sum]
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: account_scope
                      - New property: enable_api_key_provisioning
                      - New property: enable_resource_limit_change_requests
                      - New property: enable_scim_entitlements
                      - New property: heappe_identifier
                      - New property: hide_api_keys_tab
                      - New property: scim_login_nodes
                      - New property: uses_robot_accounts
                      - Modified property: disable_autoapprove
                        - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                      - Modified property: heappe_cluster_id
                        - Nullable changed from false to true
                      - Modified property: heappe_local_base_path
                        - Nullable changed from false to true
                      - Modified property: heappe_url
                        - Nullable changed from false to true
                      - Modified property: heappe_username
                        - Nullable changed from false to true
                      - Modified property: homedir_prefix
                        - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                        - Default changed from '/home/' to null
                      - Modified property: login_shell
                        - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                        - Default changed from '/bin/bash' to null
                      - Modified property: project_permanent_directory
                        - Nullable changed from false to true
                      - Modified property: scratch_project_directory
                        - Nullable changed from false to true
                      - Modified property: username_anonymized_prefix
                        - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                        - Default changed from 'waldur_' to null
                      - Modified property: username_generation_policy
                        - Property 'OneOf' changed
                          - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                        - Property 'AllOf' changed
                          - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                        - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                        - Default changed from 'service_provider' to null
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: component_formula_config
                            - New property: component_sum_config
                            - New property: pattern
                            - New property: pattern_error
                            - New property: unique
                            - New property: visible_if
                            - Modified property: default_configs
                              - Properties changed
                                - New property: load_balancer_mode
                                - New property: topology_mode
                            - Modified property: type
                              - New enum values: [component_formula component_sum]
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - New property: order_notification_emails
                      - New property: order_notification_roles
                      - Modified property: heappe_cluster_password
                        - Nullable changed from false to true
                      - Modified property: heappe_password
                        - Nullable changed from false to true
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: catalog
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/CatalogSummary
                          - Properties changed
                            - New property: supports_cpu_target_restrictions

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: limit_decimal_places
                - Modified property: default_limit
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: limit_amount
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: max_available_limit
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: max_value
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: min_value
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: component_formula_config
                    - New property: component_sum_config
                    - New property: pattern
                    - New property: pattern_error
                    - New property: unique
                    - New property: visible_if
                    - Modified property: default_configs
                      - Properties changed
                        - New property: load_balancer_mode
                        - New property: topology_mode
                    - Modified property: type
                      - New enum values: [component_formula component_sum]
          - Modified property: plans
            - Items changed
              - Properties changed
                - New property: billing_mode
          - Modified property: plugin_options
            - Properties changed
              - New property: account_scope
              - New property: enable_api_key_provisioning
              - New property: enable_resource_limit_change_requests
              - New property: enable_scim_entitlements
              - New property: heappe_identifier
              - New property: hide_api_keys_tab
              - New property: scim_login_nodes
              - New property: uses_robot_accounts
              - Modified property: disable_autoapprove
                - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
              - Modified property: heappe_cluster_id
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_local_base_path
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_url
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_username
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: homedir_prefix
                - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                - Default changed from '/home/' to null
                - MinLength changed from 1 to 0
              - Modified property: login_shell
                - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                - Default changed from '/bin/bash' to null
                - MinLength changed from 1 to 0
              - Modified property: project_permanent_directory
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: scratch_project_directory
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: username_anonymized_prefix
                - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                - Default changed from 'waldur_' to null
                - MinLength changed from 1 to 0
              - Modified property: username_generation_policy
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                - Property 'AllOf' changed
                  - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                - Default changed from 'service_provider' to null
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: component_formula_config
                    - New property: component_sum_config
                    - New property: pattern
                    - New property: pattern_error
                    - New property: unique
                    - New property: visible_if
                    - Modified property: default_configs
                      - Properties changed
                        - New property: load_balancer_mode
                        - New property: topology_mode
                    - Modified property: type
                      - New enum values: [component_formula component_sum]
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: limit_decimal_places
                - Modified property: default_limit
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: limit_amount
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: max_available_limit
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: max_value
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: min_value
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: component_formula_config
                    - New property: component_sum_config
                    - New property: pattern
                    - New property: pattern_error
                    - New property: unique
                    - New property: visible_if
                    - Modified property: default_configs
                      - Properties changed
                        - New property: load_balancer_mode
                        - New property: topology_mode
                    - Modified property: type
                      - New enum values: [component_formula component_sum]
          - Modified property: plans
            - Items changed
              - Properties changed
                - New property: billing_mode
          - Modified property: plugin_options
            - Properties changed
              - New property: account_scope
              - New property: enable_api_key_provisioning
              - New property: enable_resource_limit_change_requests
              - New property: enable_scim_entitlements
              - New property: heappe_identifier
              - New property: hide_api_keys_tab
              - New property: scim_login_nodes
              - New property: uses_robot_accounts
              - Modified property: disable_autoapprove
                - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
              - Modified property: heappe_cluster_id
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_local_base_path
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_url
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_username
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: homedir_prefix
                - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                - Default changed from '/home/' to null
                - MinLength changed from 1 to 0
              - Modified property: login_shell
                - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                - Default changed from '/bin/bash' to null
                - MinLength changed from 1 to 0
              - Modified property: project_permanent_directory
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: scratch_project_directory
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: username_anonymized_prefix
                - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                - Default changed from 'waldur_' to null
                - MinLength changed from 1 to 0
              - Modified property: username_generation_policy
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                - Property 'AllOf' changed
                  - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                - Default changed from 'service_provider' to null
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: component_formula_config
                    - New property: component_sum_config
                    - New property: pattern
                    - New property: pattern_error
                    - New property: unique
                    - New property: visible_if
                    - Modified property: default_configs
                      - Properties changed
                        - New property: load_balancer_mode
                        - New property: topology_mode
                    - Modified property: type
                      - New enum values: [component_formula component_sum]
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: limit_decimal_places
                - Modified property: default_limit
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: limit_amount
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: max_available_limit
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: max_value
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
                - Modified property: min_value
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
                  - ExclusiveMin changed from null to true
                  - ExclusiveMax changed from null to true
                  - Min changed from -2.147483648e+09 to -1e+18
                  - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: component_formula_config
                    - New property: component_sum_config
                    - New property: pattern
                    - New property: pattern_error
                    - New property: unique
                    - New property: visible_if
                    - Modified property: default_configs
                      - Properties changed
                        - New property: load_balancer_mode
                        - New property: topology_mode
                    - Modified property: type
                      - New enum values: [component_formula component_sum]
          - Modified property: plans
            - Items changed
              - Properties changed
                - New property: billing_mode
          - Modified property: plugin_options
            - Properties changed
              - New property: account_scope
              - New property: enable_api_key_provisioning
              - New property: enable_resource_limit_change_requests
              - New property: enable_scim_entitlements
              - New property: heappe_identifier
              - New property: hide_api_keys_tab
              - New property: scim_login_nodes
              - New property: uses_robot_accounts
              - Modified property: disable_autoapprove
                - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
              - Modified property: heappe_cluster_id
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_local_base_path
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_url
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_username
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: homedir_prefix
                - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                - Default changed from '/home/' to null
                - MinLength changed from 1 to 0
              - Modified property: login_shell
                - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                - Default changed from '/bin/bash' to null
                - MinLength changed from 1 to 0
              - Modified property: project_permanent_directory
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: scratch_project_directory
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: username_anonymized_prefix
                - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                - Default changed from 'waldur_' to null
                - MinLength changed from 1 to 0
              - Modified property: username_generation_policy
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                - Property 'AllOf' changed
                  - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                - Default changed from 'service_provider' to null
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: component_formula_config
                    - New property: component_sum_config
                    - New property: pattern
                    - New property: pattern_error
                    - New property: unique
                    - New property: visible_if
                    - Modified property: default_configs
                      - Properties changed
                        - New property: load_balancer_mode
                        - New property: topology_mode
                    - Modified property: type
                      - New enum values: [component_formula component_sum]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_settings
            - New property: billing_mode_components
            - New property: billing_period_applies
            - New property: can_update_integration
            - New property: can_update_options
            - New property: compliance_checklist_details
            - New property: limit_precision_advisory
            - New property: scope_resource
            - New property: scope_resource_name
            - New property: scope_resource_uuid
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: billing_mode
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: billing_type
                        - New property: is_prepaid
                        - New property: limit_period
                        - Modified property: measured_unit
                          - Description changed from 'Unit of measurement, for example, GB.' to ''
                          - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: order_notification_emails
                    - New property: order_notification_roles
                    - Modified property: heappe_cluster_password
                      - Nullable changed from false to true
                    - Modified property: heappe_password
                      - Nullable changed from false to true
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/CatalogSummary
                        - Properties changed
                          - New property: supports_cpu_target_restrictions

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
                  - Modified property: plans
                    - Items changed
                      - Properties changed
                        - New property: billing_mode

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_settings billing_mode_components billing_period_applies can_update_integration can_update_options compliance_checklist_details limit_precision_advisory scope_resource scope_resource_name scope_resource_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_settings
            - New property: billing_mode_components
            - New property: billing_period_applies
            - New property: can_update_integration
            - New property: can_update_options
            - New property: compliance_checklist_details
            - New property: limit_precision_advisory
            - New property: scope_resource
            - New property: scope_resource_name
            - New property: scope_resource_uuid
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: billing_mode
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: billing_type
                        - New property: is_prepaid
                        - New property: limit_period
                        - Modified property: measured_unit
                          - Description changed from 'Unit of measurement, for example, GB.' to ''
                          - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: order_notification_emails
                    - New property: order_notification_roles
                    - Modified property: heappe_cluster_password
                      - Nullable changed from false to true
                    - Modified property: heappe_password
                      - Nullable changed from false to true
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/CatalogSummary
                        - Properties changed
                          - New property: supports_cpu_target_restrictions

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- Description changed from 'Returns monthly usage statistics for the components of an offering within a specified date range.' to 'Returns monthly usage statistics for the components of an offering within a specified date range. Requires SERVICE_PROVIDER.GET_STATISTICS on the offering's customer or its service provider, or ORDER.LIST on the offering, its customer, or that customer's service provider.'

GET /api/marketplace-provider-offerings/{uuid}/costs/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: limit_decimal_places
          - Modified property: default_limit
            - Type changed from 'integer' to 'number'
            - Format changed from '' to 'double'
            - ExclusiveMin changed from null to true
            - ExclusiveMax changed from null to true
            - Min changed from -2.147483648e+09 to -1e+18
            - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: limit_amount
            - Type changed from 'integer' to 'number'
            - Format changed from '' to 'double'
            - ExclusiveMin changed from null to true
            - ExclusiveMax changed from null to true
            - Min changed from -2.147483648e+09 to -1e+18
            - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: max_available_limit
            - Type changed from 'integer' to 'number'
            - Format changed from '' to 'double'
            - ExclusiveMin changed from null to true
            - ExclusiveMax changed from null to true
            - Min changed from -2.147483648e+09 to -1e+18
            - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: max_value
            - Type changed from 'integer' to 'number'
            - Format changed from '' to 'double'
            - ExclusiveMin changed from null to true
            - ExclusiveMax changed from null to true
            - Min changed from -2.147483648e+09 to -1e+18
            - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: min_value
            - Type changed from 'integer' to 'number'
            - Format changed from '' to 'double'
            - ExclusiveMin changed from null to true
            - ExclusiveMax changed from null to true
            - Min changed from -2.147483648e+09 to -1e+18
            - Max changed from 2.147483647e+09 to 1e+18

GET /api/marketplace-provider-offerings/{uuid}/customers/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/effective_posix_id_pool/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [group_gid_used group_gid_utilization max_group_gid min_group_gid next_group_gid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: group_gid_used
            - New property: group_gid_utilization
            - New property: max_group_gid
            - New property: min_group_gid
            - New property: next_group_gid

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
                    - Modified property: plans
                      - Items changed
                        - Properties changed
                          - New property: billing_mode

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
                    - New enum values: [provider_project]
            - Modified property: users
              - Items changed
                - Properties changed
                  - Modified property: memberships
                    - Items changed
                      - Properties changed
                        - Modified property: kind
                          - New enum values: [provider_project]

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_account_settings
            - New property: project_start_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
            - Modified property: is_limit_based
              - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
            - Modified property: is_usage_based
              - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: user_uuid
                - Nullable changed from false to true
              - Modified property: username
                - Nullable changed from false to true

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_metrics]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_metrics
              - Modified property: project_metadata
                - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
                - Items changed
                  - Properties changed
                    - New property: modified
              - Modified property: slug
                - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [details has_passkey passkey_count]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: details
              - New property: has_passkey
              - New property: passkey_count
              - Modified property: permissions
                - Items changed
                  - Properties changed
                    - New property: source
                    - Modified property: customer_name
                      - Nullable changed from false to true
                    - Modified property: customer_uuid
                      - Nullable changed from false to true

GET /api/marketplace-provider-offerings/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source

HEAD /api/marketplace-provider-offerings/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_settings
            - New property: billing_mode_components
            - New property: billing_period_applies
            - New property: can_update_integration
            - New property: can_update_options
            - New property: compliance_checklist_details
            - New property: scope_resource
            - New property: scope_resource_name
            - New property: scope_resource_uuid
            - New property: user_has_offering_user
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: billing_mode
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: billing_type
                        - New property: is_prepaid
                        - New property: limit_period
                        - Modified property: measured_unit
                          - Description changed from 'Unit of measurement, for example, GB.' to ''
                          - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/CatalogSummary
                        - Properties changed
                          - New property: supports_cpu_target_restrictions

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [new_plan_billing_mode old_plan_billing_mode resource_end_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: new_plan_billing_mode
              - New property: old_plan_billing_mode
              - New property: resource_end_date
              - Modified property: limits
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: old_cost_estimate
                - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [new_plan_billing_mode old_plan_billing_mode resource_end_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: new_plan_billing_mode
            - New property: old_plan_billing_mode
            - New property: resource_end_date
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: old_cost_estimate
              - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/marketplace-provider-offerings/{uuid}/state_counters/

- Description changed from 'Returns resource and offering-user counts grouped by state for the given offering.' to 'Returns resource and offering-user counts grouped by state for the given offering. Requires SERVICE_PROVIDER.GET_STATISTICS on the offering's customer or its service provider, or ORDER.LIST on the offering, its customer, or that customer's service provider.'

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: account_scope
              - New property: enable_api_key_provisioning
              - New property: enable_resource_limit_change_requests
              - New property: enable_scim_entitlements
              - New property: heappe_identifier
              - New property: hide_api_keys_tab
              - New property: scim_login_nodes
              - New property: uses_robot_accounts
              - Modified property: disable_autoapprove
                - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
              - Modified property: heappe_cluster_id
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_local_base_path
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_url
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_username
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: homedir_prefix
                - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                - Default changed from '/home/' to null
                - MinLength changed from 1 to 0
              - Modified property: login_shell
                - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                - Default changed from '/bin/bash' to null
                - MinLength changed from 1 to 0
              - Modified property: project_permanent_directory
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: scratch_project_directory
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: username_anonymized_prefix
                - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                - Default changed from 'waldur_' to null
                - MinLength changed from 1 to 0
              - Modified property: username_generation_policy
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                - Property 'AllOf' changed
                  - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                - Default changed from 'service_provider' to null
          - Modified property: secret_options
            - Properties changed
              - New property: order_notification_emails
              - New property: order_notification_roles
              - Modified property: heappe_cluster_password
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
              - Modified property: heappe_password
                - Nullable changed from false to true
                - MinLength changed from 1 to 0

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: limit_decimal_places
          - Modified property: default_limit
            - Type changed from 'integer' to 'number'
            - Format changed from '' to 'double'
            - ExclusiveMin changed from null to true
            - ExclusiveMax changed from null to true
            - Min changed from -2.147483648e+09 to -1e+18
            - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: limit_amount
            - Type changed from 'integer' to 'number'
            - Format changed from '' to 'double'
            - ExclusiveMin changed from null to true
            - ExclusiveMax changed from null to true
            - Min changed from -2.147483648e+09 to -1e+18
            - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: max_available_limit
            - Type changed from 'integer' to 'number'
            - Format changed from '' to 'double'
            - ExclusiveMin changed from null to true
            - ExclusiveMax changed from null to true
            - Min changed from -2.147483648e+09 to -1e+18
            - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: max_value
            - Type changed from 'integer' to 'number'
            - Format changed from '' to 'double'
            - ExclusiveMin changed from null to true
            - ExclusiveMax changed from null to true
            - Min changed from -2.147483648e+09 to -1e+18
            - Max changed from 2.147483647e+09 to 1e+18
          - Modified property: min_value
            - Type changed from 'integer' to 'number'
            - Format changed from '' to 'double'
            - ExclusiveMin changed from null to true
            - ExclusiveMax changed from null to true
            - Min changed from -2.147483648e+09 to -1e+18
            - Max changed from 2.147483647e+09 to 1e+18

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
                    - New property: component_formula_config
                    - New property: component_sum_config
                    - New property: pattern
                    - New property: pattern_error
                    - New property: unique
                    - New property: visible_if
                    - Modified property: default_configs
                      - Properties changed
                        - New property: load_balancer_mode
                        - New property: topology_mode
                    - Modified property: type
                      - New enum values: [component_formula component_sum]

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
                    - New property: component_formula_config
                    - New property: component_sum_config
                    - New property: pattern
                    - New property: pattern_error
                    - New property: unique
                    - New property: visible_if
                    - Modified property: default_configs
                      - Properties changed
                        - New property: load_balancer_mode
                        - New property: topology_mode
                    - Modified property: type
                      - New enum values: [component_formula component_sum]

GET /api/marketplace-provider-resource-projects/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source
              - New property: user_active_isds
              - New property: user_address
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
              - New property: user_organization_address
              - New property: user_organization_country
              - New property: user_organization_registry_code
              - New property: user_organization_type
              - New property: user_organization_vat_code
              - New property: user_personal_title
              - New property: user_phone_number
              - New property: user_place_of_birth
              - New property: user_primary_gid
              - New property: user_uid_number

HEAD /api/marketplace-provider-resource-projects/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

GET /api/marketplace-provider-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_account_settings project_start_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_account_settings
              - New property: project_start_date
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: new_plan_billing_mode
                      - New property: old_plan_billing_mode
                      - New property: resource_end_date
                      - Modified property: limits
                        - AdditionalProperties changed
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                      - Modified property: old_cost_estimate
                        - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
              - Modified property: is_limit_based
                - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
              - Modified property: is_usage_based
                - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
              - Modified property: limits
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: new_plan_billing_mode
                      - New property: old_plan_billing_mode
                      - New property: resource_end_date
                      - Modified property: limits
                        - AdditionalProperties changed
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                      - Modified property: old_cost_estimate
                        - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_account_settings project_start_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_account_settings
            - New property: project_start_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
            - Modified property: is_limit_based
              - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
            - Modified property: is_usage_based
              - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

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
                    - New enum values: [provider_project]
            - Modified property: users
              - Items changed
                - Properties changed
                  - Modified property: memberships
                    - Items changed
                      - Properties changed
                        - Modified property: kind
                          - New enum values: [provider_project]

GET /api/marketplace-provider-resources/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source
              - New property: user_active_isds
              - New property: user_address
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
              - New property: user_organization_address
              - New property: user_organization_country
              - New property: user_organization_registry_code
              - New property: user_organization_type
              - New property: user_organization_vat_code
              - New property: user_personal_title
              - New property: user_phone_number
              - New property: user_place_of_birth
              - New property: user_primary_gid
              - New property: user_uid_number

HEAD /api/marketplace-provider-resources/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_account_settings
            - New property: project_start_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
            - Modified property: is_limit_based
              - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
            - Modified property: is_usage_based
              - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/marketplace-provider-resources/{uuid}/offering/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_settings billing_mode_components billing_period_applies can_update_integration can_update_options compliance_checklist_details scope_resource scope_resource_name scope_resource_uuid user_has_offering_user]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_settings
            - New property: billing_mode_components
            - New property: billing_period_applies
            - New property: can_update_integration
            - New property: can_update_options
            - New property: compliance_checklist_details
            - New property: scope_resource
            - New property: scope_resource_name
            - New property: scope_resource_uuid
            - New property: user_has_offering_user
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: billing_mode
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: billing_type
                        - New property: is_prepaid
                        - New property: limit_period
                        - Modified property: measured_unit
                          - Description changed from 'Unit of measurement, for example, GB.' to ''
                          - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/CatalogSummary
                        - Properties changed
                          - New property: supports_cpu_target_restrictions

GET /api/marketplace-provider-resources/{uuid}/plan_periods/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Required changed
                    - New required property: recurring
                  - Properties changed
                    - New property: missing_usage_policy
                    - Modified property: recurring
                      - Description changed from 'Reported value is reused every month until changed.' to 'Deprecated, use missing_usage_policy instead. True when the reported value is reused every month until changed.'
                      - ReadOnly changed from false to true

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'

POST /api/marketplace-provider-resources/{uuid}/set_as_ok/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'

POST /api/marketplace-provider-resources/{uuid}/set_backend_metadata/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'

POST /api/marketplace-provider-resources/{uuid}/set_endpoints/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'

POST /api/marketplace-provider-resources/{uuid}/set_limits/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'

POST /api/marketplace-provider-resources/{uuid}/set_membership_sync_statuses/

- Description changed from 'Full-replace report from the site agent: replaces every previously stored member sync status of this resource with the submitted set. Requires the offering to opt in via the enable_membership_sync_status plugin option. Entries whose user cannot be resolved are skipped and echoed back in the response instead of failing the whole report.' to 'Complete report from the site agent: afterwards the resource's stored member sync statuses are exactly the submitted set. Only the differences are written; unchanged statuses are left as they are, and the report time is recorded once per resource. Requires the offering to opt in via the enable_membership_sync_status plugin option. Entries whose user cannot be resolved are skipped and echoed back in the response instead of failing the whole report.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: statuses
            - Items changed
              - Properties changed
                - Modified property: role_name
                  - MaxLength changed from null to 150

POST /api/marketplace-provider-resources/{uuid}/set_slug/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Updates the slug for a resource. Requires staff permissions.' to 'Updates the slug of a resource. Requires staff or the RESOURCE.SET_SLUG permission, which no role holds unless the deployment grants it. Other than staff, a holder cannot change the slug once the resource's creation order is executing or the resource exists in the backend.'

POST /api/marketplace-provider-resources/{uuid}/submit_report/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'

POST /api/marketplace-provider-resources/{uuid}/update_options_direct/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'

GET /api/marketplace-public-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_settings billing_mode_components billing_period_applies can_update_integration can_update_options compliance_checklist_details scope_resource scope_resource_name scope_resource_uuid user_has_offering_user]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: account_settings
              - New property: billing_mode_components
              - New property: billing_period_applies
              - New property: can_update_integration
              - New property: can_update_options
              - New property: compliance_checklist_details
              - New property: scope_resource
              - New property: scope_resource_name
              - New property: scope_resource_uuid
              - New property: user_has_offering_user
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: component_formula_config
                            - New property: component_sum_config
                            - New property: pattern
                            - New property: pattern_error
                            - New property: unique
                            - New property: visible_if
                            - Modified property: default_configs
                              - Properties changed
                                - New property: load_balancer_mode
                                - New property: topology_mode
                            - Modified property: type
                              - New enum values: [component_formula component_sum]
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: account_scope
                      - New property: enable_api_key_provisioning
                      - New property: enable_resource_limit_change_requests
                      - New property: enable_scim_entitlements
                      - New property: heappe_identifier
                      - New property: hide_api_keys_tab
                      - New property: scim_login_nodes
                      - New property: uses_robot_accounts
                      - Modified property: disable_autoapprove
                        - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                      - Modified property: heappe_cluster_id
                        - Nullable changed from false to true
                      - Modified property: heappe_local_base_path
                        - Nullable changed from false to true
                      - Modified property: heappe_url
                        - Nullable changed from false to true
                      - Modified property: heappe_username
                        - Nullable changed from false to true
                      - Modified property: homedir_prefix
                        - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                        - Default changed from '/home/' to null
                      - Modified property: login_shell
                        - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                        - Default changed from '/bin/bash' to null
                      - Modified property: project_permanent_directory
                        - Nullable changed from false to true
                      - Modified property: scratch_project_directory
                        - Nullable changed from false to true
                      - Modified property: username_anonymized_prefix
                        - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                        - Default changed from 'waldur_' to null
                      - Modified property: username_generation_policy
                        - Property 'OneOf' changed
                          - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                        - Property 'AllOf' changed
                          - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                        - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                        - Default changed from 'service_provider' to null
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: component_formula_config
                            - New property: component_sum_config
                            - New property: pattern
                            - New property: pattern_error
                            - New property: unique
                            - New property: visible_if
                            - Modified property: default_configs
                              - Properties changed
                                - New property: load_balancer_mode
                                - New property: topology_mode
                            - Modified property: type
                              - New enum values: [component_formula component_sum]
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: catalog
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/CatalogSummary
                          - Properties changed
                            - New property: supports_cpu_target_restrictions

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_settings billing_mode_components billing_period_applies can_update_integration can_update_options compliance_checklist_details scope_resource scope_resource_name scope_resource_uuid user_has_offering_user]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_settings
            - New property: billing_mode_components
            - New property: billing_period_applies
            - New property: can_update_integration
            - New property: can_update_options
            - New property: compliance_checklist_details
            - New property: scope_resource
            - New property: scope_resource_name
            - New property: scope_resource_uuid
            - New property: user_has_offering_user
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: billing_mode
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: billing_type
                        - New property: is_prepaid
                        - New property: limit_period
                        - Modified property: measured_unit
                          - Description changed from 'Unit of measurement, for example, GB.' to ''
                          - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/CatalogSummary
                        - Properties changed
                          - New property: supports_cpu_target_restrictions

GET /api/marketplace-public-offerings/{uuid}/plans/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: billing_mode
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: billing_type
                    - New property: is_prepaid
                    - New property: limit_period
                    - Modified property: measured_unit
                      - Description changed from 'Unit of measurement, for example, GB.' to ''
                      - Nullable changed from false to true

GET /api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_mode
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: billing_type
                  - New property: is_prepaid
                  - New property: limit_period
                  - Modified property: measured_unit
                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                    - Nullable changed from false to true

GET /api/marketplace-resource-api-keys/

- New query param: has_pending_action
- New query param: pending_action
- New query param: user_uuid
- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Paused Deleting Deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: allowed_models
              - New required property: current_usages
              - New required property: limits
              - New required property: paused_by_limit
              - New required property: pending_action
              - New required property: usage_period
              - New required property: user_full_name
              - New required property: user_uuid
            - Properties changed
              - New property: allowed_models
              - New property: current_usages
              - New property: issued_at
              - New property: limits
              - New property: paused_by_limit
              - New property: pending_action
              - New property: usage_period
              - New property: user_full_name
              - New property: user_uuid
              - Modified property: state
                - New enum values: [Paused Deleting Deleted]

HEAD /api/marketplace-resource-api-keys/

- New query param: has_pending_action
- New query param: pending_action
- New query param: user_uuid
- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Paused Deleting Deleted]

POST /api/marketplace-resource-api-keys/report_created/

- Description changed from 'Used by the site agent after it generated and applied a key to the backend. Stores the value encrypted and marks the key OK.' to 'Used by the site agent after it generated and applied a key to the backend at provisioning. Stores the value encrypted and marks the key OK. A requested key is reported through set_key instead.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_models
            - New required property: current_usages
            - New required property: limits
            - New required property: paused_by_limit
            - New required property: pending_action
            - New required property: usage_period
            - New required property: user_full_name
            - New required property: user_uuid
          - Properties changed
            - New property: allowed_models
            - New property: current_usages
            - New property: issued_at
            - New property: limits
            - New property: paused_by_limit
            - New property: pending_action
            - New property: usage_period
            - New property: user_full_name
            - New property: user_uuid
            - Modified property: state
              - New enum values: [Paused Deleting Deleted]

GET /api/marketplace-resource-api-keys/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_models
            - New required property: current_usages
            - New required property: limits
            - New required property: paused_by_limit
            - New required property: pending_action
            - New required property: usage_period
            - New required property: user_full_name
            - New required property: user_uuid
          - Properties changed
            - New property: allowed_models
            - New property: current_usages
            - New property: issued_at
            - New property: limits
            - New property: paused_by_limit
            - New property: pending_action
            - New property: usage_period
            - New property: user_full_name
            - New property: user_uuid
            - Modified property: state
              - New enum values: [Paused Deleting Deleted]

GET /api/marketplace-resource-api-keys/{uuid}/reveal/

- Description changed from 'Returns the decrypted key value. Available to users with resource access (except minimal-visibility viewers). Audit-logged.' to 'Returns the decrypted key value. Available to users with resource access (except minimal-visibility viewers); a key with an assignee only to the assignee. Staff and support always. Audit-logged.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_models
            - New required property: current_usages
            - New required property: limits
            - New required property: paused_by_limit
            - New required property: pending_action
            - New required property: usage_period
            - New required property: user_full_name
            - New required property: user_uuid
          - Properties changed
            - New property: allowed_models
            - New property: current_usages
            - New property: issued_at
            - New property: limits
            - New property: paused_by_limit
            - New property: pending_action
            - New property: usage_period
            - New property: user_full_name
            - New property: user_uuid
            - Modified property: state
              - New enum values: [Paused Deleting Deleted]

POST /api/marketplace-resource-api-keys/{uuid}/set_erred/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'resource.offering.customer' to 'resource.offering'
    - Added /0/scopes/- with value: 'resource.offering.customer'
    - Added /0/scopes/- with value: 'resource.offering.customer.serviceprovider'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_models
            - New required property: current_usages
            - New required property: limits
            - New required property: paused_by_limit
            - New required property: pending_action
            - New required property: usage_period
            - New required property: user_full_name
            - New required property: user_uuid
          - Properties changed
            - New property: allowed_models
            - New property: current_usages
            - New property: issued_at
            - New property: limits
            - New property: paused_by_limit
            - New property: pending_action
            - New property: usage_period
            - New property: user_full_name
            - New property: user_uuid
            - Modified property: state
              - New enum values: [Paused Deleting Deleted]

POST /api/marketplace-resource-api-keys/{uuid}/set_key/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'resource.offering.customer' to 'resource.offering'
    - Added /0/scopes/- with value: 'resource.offering.customer'
    - Added /0/scopes/- with value: 'resource.offering.customer.serviceprovider'
- Summary changed from 'Report a rotated API key value' to 'Report a created or rotated API key value'
- Description changed from 'Used by the site agent after it applied a rotated key. Replaces the stored value and marks the key OK.' to 'Used by the site agent after it applied a requested or rotated key. Replaces the stored value and marks the key OK. A requested key carries the client_id the agent gave it.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_models
            - New required property: current_usages
            - New required property: limits
            - New required property: paused_by_limit
            - New required property: pending_action
            - New required property: usage_period
            - New required property: user_full_name
            - New required property: user_uuid
          - Properties changed
            - New property: allowed_models
            - New property: current_usages
            - New property: issued_at
            - New property: limits
            - New property: paused_by_limit
            - New property: pending_action
            - New property: usage_period
            - New property: user_full_name
            - New property: user_uuid
            - Modified property: state
              - New enum values: [Paused Deleting Deleted]

POST /api/marketplace-resource-limit-change-requests/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: requested_limits
            - AdditionalProperties changed from true to null
            - AdditionalProperties changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_limits
              - AdditionalProperties changed from true to null
              - AdditionalProperties changed
                - Schema added

GET /api/marketplace-resource-projects/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source

HEAD /api/marketplace-resource-projects/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

GET /api/marketplace-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_account_settings project_start_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_account_settings
              - New property: project_start_date
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: new_plan_billing_mode
                      - New property: old_plan_billing_mode
                      - New property: resource_end_date
                      - Modified property: limits
                        - AdditionalProperties changed
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                      - Modified property: old_cost_estimate
                        - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
              - Modified property: is_limit_based
                - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
              - Modified property: is_usage_based
                - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
              - Modified property: limits
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: new_plan_billing_mode
                      - New property: old_plan_billing_mode
                      - New property: resource_end_date
                      - Modified property: limits
                        - AdditionalProperties changed
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                      - Modified property: old_cost_estimate
                        - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_account_settings project_start_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_account_settings
            - New property: project_start_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
            - Modified property: is_limit_based
              - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
            - Modified property: is_usage_based
              - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

POST /api/marketplace-resources/{uuid}/estimate_renewal/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'

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
                    - New enum values: [provider_project]
            - Modified property: users
              - Items changed
                - Properties changed
                  - Modified property: memberships
                    - Items changed
                      - Properties changed
                        - Modified property: kind
                          - New enum values: [provider_project]

GET /api/marketplace-resources/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source

HEAD /api/marketplace-resources/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_account_settings
            - New property: project_start_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
            - Modified property: is_limit_based
              - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
            - Modified property: is_usage_based
              - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: new_plan_billing_mode
                    - New property: old_plan_billing_mode
                    - New property: resource_end_date
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: old_cost_estimate
                      - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/marketplace-resources/{uuid}/offering/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_settings billing_mode_components billing_period_applies can_update_integration can_update_options compliance_checklist_details scope_resource scope_resource_name scope_resource_uuid user_has_offering_user]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_settings
            - New property: billing_mode_components
            - New property: billing_period_applies
            - New property: can_update_integration
            - New property: can_update_options
            - New property: compliance_checklist_details
            - New property: scope_resource
            - New property: scope_resource_name
            - New property: scope_resource_uuid
            - New property: user_has_offering_user
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: billing_mode
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: billing_type
                        - New property: is_prepaid
                        - New property: limit_period
                        - Modified property: measured_unit
                          - Description changed from 'Unit of measurement, for example, GB.' to ''
                          - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/CatalogSummary
                        - Properties changed
                          - New property: supports_cpu_target_restrictions

GET /api/marketplace-resources/{uuid}/plan_periods/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Required changed
                    - New required property: recurring
                  - Properties changed
                    - New property: missing_usage_policy
                    - Modified property: recurring
                      - Description changed from 'Reported value is reused every month until changed.' to 'Deprecated, use missing_usage_policy instead. True when the reported value is reused every month until changed.'
                      - ReadOnly changed from false to true

POST /api/marketplace-resources/{uuid}/reallocate_limits/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
              - Min changed from 1 to 0
          - Modified property: targets
            - Items changed
              - Properties changed
                - Modified property: allocated_limits
                  - AdditionalProperties changed
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - Min changed from 1 to 0

POST /api/marketplace-resources/{uuid}/renew/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'

POST /api/marketplace-resources/{uuid}/set_slug/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Updates the slug for a resource. Requires staff permissions.' to 'Updates the slug of a resource. Requires staff or the RESOURCE.SET_SLUG permission, which no role holds unless the deployment grants it. Other than staff, a holder cannot change the slug once the resource's creation order is executing or the resource exists in the backend.'

POST /api/marketplace-resources/{uuid}/update_limits/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'

GET /api/marketplace-robot-accounts/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [resource_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: resource_backend_id
              - Modified property: offering_plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: account_scope
                      - New property: enable_api_key_provisioning
                      - New property: enable_resource_limit_change_requests
                      - New property: enable_scim_entitlements
                      - New property: heappe_identifier
                      - New property: hide_api_keys_tab
                      - New property: scim_login_nodes
                      - New property: uses_robot_accounts
                      - Modified property: disable_autoapprove
                        - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                      - Modified property: heappe_cluster_id
                        - Nullable changed from false to true
                      - Modified property: heappe_local_base_path
                        - Nullable changed from false to true
                      - Modified property: heappe_url
                        - Nullable changed from false to true
                      - Modified property: heappe_username
                        - Nullable changed from false to true
                      - Modified property: homedir_prefix
                        - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                        - Default changed from '/home/' to null
                      - Modified property: login_shell
                        - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                        - Default changed from '/bin/bash' to null
                      - Modified property: project_permanent_directory
                        - Nullable changed from false to true
                      - Modified property: scratch_project_directory
                        - Nullable changed from false to true
                      - Modified property: username_anonymized_prefix
                        - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                        - Default changed from 'waldur_' to null
                      - Modified property: username_generation_policy
                        - Property 'OneOf' changed
                          - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                        - Property 'AllOf' changed
                          - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                        - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                        - Default changed from 'service_provider' to null

GET /api/marketplace-robot-accounts/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [resource_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_backend_id
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_backend_id
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_backend_id
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_backend_id
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_backend_id
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_backend_id
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: account_scope
                    - New property: enable_api_key_provisioning
                    - New property: enable_resource_limit_change_requests
                    - New property: enable_scim_entitlements
                    - New property: heappe_identifier
                    - New property: hide_api_keys_tab
                    - New property: scim_login_nodes
                    - New property: uses_robot_accounts
                    - Modified property: disable_autoapprove
                      - Description changed from 'If set to True, orders for this offering will always require manual approval, overriding auto_approve_in_service_provider_projects' to 'If set to True, orders for this offering will always require manual consumer approval, overriding every other consumer-side auto-approve mechanism (auto_approve_in_service_provider_projects, auto_approve_for_roles, project auto-approval rules, and the ORDER.APPROVE permission). Termination orders, staff users and provider approval are not affected'
                    - Modified property: heappe_cluster_id
                      - Nullable changed from false to true
                    - Modified property: heappe_local_base_path
                      - Nullable changed from false to true
                    - Modified property: heappe_url
                      - Nullable changed from false to true
                    - Modified property: heappe_username
                      - Nullable changed from false to true
                    - Modified property: homedir_prefix
                      - Description changed from 'GLAuth homedir prefix' to 'Prefix of each account's home directory; the username follows.'
                      - Default changed from '/home/' to null
                    - Modified property: login_shell
                      - Description changed from 'Default login shell assigned to GLAuth/LDAP accounts.' to 'Login shell assigned to GLAuth/LDAP accounts.'
                      - Default changed from '/bin/bash' to null
                    - Modified property: project_permanent_directory
                      - Nullable changed from false to true
                    - Modified property: scratch_project_directory
                      - Nullable changed from false to true
                    - Modified property: username_anonymized_prefix
                      - Description changed from 'GLAuth prefix for anonymized usernames' to 'Prefix for anonymized usernames; the name is the prefix followed by the account's POSIX UID.'
                      - Default changed from 'waldur_' to null
                    - Modified property: username_generation_policy
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/UsernameGenerationPolicyEnum, #/components/schemas/BlankEnum
                      - Property 'AllOf' changed
                        - Schemas deleted: #/components/schemas/UsernameGenerationPolicyEnum
                      - Description changed from 'GLAuth username generation policy' to 'How the usernames of offering users are generated.'
                      - Default changed from 'service_provider' to null

GET /api/marketplace-runtime-states/

- Description changed from '
        Returns a unique, sorted list of runtime states for all resources accessible to the current user.
        The runtime state is a backend-specific state of a resource (e.g., 'ACTIVE', 'SHUTOFF' for a VM).
        This endpoint is useful for building dynamic filters in a user interface.
        The list can be optionally filtered by project or category.
        ' to '
        Returns a unique, sorted list of runtime states for resources accessible to the current user.
        The runtime state is a backend-specific state of a resource (e.g., 'ACTIVE', 'SHUTOFF' for a VM).
        This endpoint is useful for building dynamic filters in a user interface.

        At least one scope query parameter is required: `project_uuid`, `category_uuid`,
        `offering_uuid`, or `customer_uuid`.
        '
- New query param: customer_uuid

GET /api/marketplace-service-providers/

- New query param: created
- New query param: created_before
- New query param: modified
- New query param: modified_before
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_options]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: account_options

HEAD /api/marketplace-service-providers/

- New query param: created
- New query param: created_before
- New query param: modified
- New query param: modified_before

POST /api/marketplace-service-providers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: account_options
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: account_options
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: account_options
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_options

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: user_uuid
                - Nullable changed from false to true
              - Modified property: username
                - Nullable changed from false to true

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
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - New property: order_notification_emails
                      - New property: order_notification_roles
                      - Modified property: heappe_cluster_password
                        - Nullable changed from false to true
                      - Modified property: heappe_password
                        - Nullable changed from false to true

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_metrics]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_metrics
              - Modified property: project_metadata
                - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
                - Items changed
                  - Properties changed
                    - New property: modified
              - Modified property: slug
                - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

GET /api/marketplace-service-providers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [account_options]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_options

PATCH /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: account_options
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: account_options
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: account_options
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_options

PUT /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: account_options
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: account_options
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: account_options
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: account_options

GET /api/marketplace-service-providers/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source

HEAD /api/marketplace-service-providers/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

GET /api/marketplace-service-providers/{uuid}/revenue/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'customer' to '*'
    - Added /0/scopes/- with value: 'customer'

GET /api/marketplace-service-providers/{uuid}/stat/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'customer' to '*'
    - Added /0/scopes/- with value: 'customer'

GET /api/marketplace-site-agent-connection-stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: agents
              - Items changed
                - Required changed
                  - New required property: auth_kind
                  - New required property: auth_token_name
                  - New required property: auth_token_prefix
                  - New required property: authorized_via
                  - New required property: delivery_blocked_reason
                  - New required property: event_consumer_uuid
                  - New required property: user_full_name
                  - New required property: user_is_staff
                  - New required property: user_username
                  - New required property: user_uuid
                - Properties changed
                  - New property: auth_kind
                  - New property: auth_token_name
                  - New property: auth_token_prefix
                  - New property: authorized_via
                  - New property: delivery_blocked_reason
                  - New property: event_consumer_uuid
                  - New property: user_full_name
                  - New property: user_is_staff
                  - New property: user_username
                  - New property: user_uuid
                  - Modified property: queues
                    - Items changed
                      - Required changed
                        - New required property: kind
                      - Properties changed
                        - New property: kind

GET /api/marketplace-site-agent-identities/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: compatibility
            - Properties changed
              - New property: compatibility

POST /api/marketplace-site-agent-identities/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: compatibility
          - Properties changed
            - New property: compatibility

GET /api/marketplace-site-agent-identities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: compatibility
          - Properties changed
            - New property: compatibility

PUT /api/marketplace-site-agent-identities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: compatibility
          - Properties changed
            - New property: compatibility

POST /api/marketplace-site-agent-identities/{uuid}/register_event_subscription/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: observable_object_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ObservableObjectTypeEnum
                - New enum values: [service_provider_account service_provider_project_group call proposal]

POST /api/marketplace-site-agent-identities/{uuid}/register_queue/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: object_types
            - Items changed
              - New enum values: [service_provider_account service_provider_project_group call proposal]

GET /api/marketplace-software-catalogs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: supports_cpu_target_restrictions
            - Properties changed
              - New property: supports_cpu_target_restrictions

POST /api/marketplace-software-catalogs/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: supports_cpu_target_restrictions
          - Properties changed
            - New property: supports_cpu_target_restrictions

GET /api/marketplace-software-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: supports_cpu_target_restrictions
          - Properties changed
            - New property: supports_cpu_target_restrictions

PATCH /api/marketplace-software-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: supports_cpu_target_restrictions
          - Properties changed
            - New property: supports_cpu_target_restrictions

PUT /api/marketplace-software-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: supports_cpu_target_restrictions
          - Properties changed
            - New property: supports_cpu_target_restrictions

GET /api/marketplace-software-packages/

- Modified query param: cpu_family
  - Description changed from 'Filter packages available for specific CPU family (e.g., x86_64, aarch64)' to 'Filter packages available for any of the given CPU families (e.g., x86_64, aarch64)'
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added
- Modified query param: cpu_microarchitecture
  - Description changed from 'Filter packages available for specific CPU microarchitecture (e.g., generic, zen2, haswell)' to 'Filter packages available for any of the given CPU microarchitectures (e.g., generic, amd/zen3, intel/sapphirerapids)'
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added

HEAD /api/marketplace-software-packages/

- Modified query param: cpu_family
  - Description changed from 'Filter packages available for specific CPU family (e.g., x86_64, aarch64)' to 'Filter packages available for any of the given CPU families (e.g., x86_64, aarch64)'
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added
- Modified query param: cpu_microarchitecture
  - Description changed from 'Filter packages available for specific CPU microarchitecture (e.g., generic, zen2, haswell)' to 'Filter packages available for any of the given CPU microarchitectures (e.g., generic, amd/zen3, intel/sapphirerapids)'
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added

GET /api/marketplace-software-targets/

- Modified query param: cpu_family
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added
- Modified query param: cpu_microarchitecture
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added

HEAD /api/marketplace-software-targets/

- Modified query param: cpu_family
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added
- Modified query param: cpu_microarchitecture
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added

GET /api/marketplace-software-versions/

- Modified query param: cpu_family
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added
- Modified query param: cpu_microarchitecture
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added

HEAD /api/marketplace-software-versions/

- Modified query param: cpu_family
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added
- Modified query param: cpu_microarchitecture
  - Style changed from '' to 'form'
  - Explode changed from null to true
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added

GET /api/marketplace-stats/resource_usage_by_customer/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: limits
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'

GET /api/matrix/credentials/

- Description changed from 'Returns Matrix login credentials for the authenticated user based on the configured login method.' to 'Returns what an external Matrix client needs to sign the authenticated user in, per MATRIX_EXTERNAL_LOGIN_METHOD. Never a password or an access token: in password mode the user generates a password with POST /api/matrix/credentials/password/.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: access_token
            - Deleted property: login_token
            - Deleted property: oidc_provider_url
            - Deleted property: password
            - Deleted property: room_id
            - Modified property: method
              - New enum values: [none password oidc]

GET /api/matrix/rooms/eligible_projects/

- Description changed from 'Returns projects where the caller is customer owner (staff sees all) and no MatrixRoom row exists yet. Existing archived rooms still block creation, so projects with any room are excluded.' to 'Returns projects where the caller holds MATRIX_ROOM.CREATE on the project or its organization (staff and support see all) and no MatrixRoom row exists yet. Existing archived rooms still block creation, so projects with any room are excluded.'

POST /api/matrix/rooms/{uuid}/export_history/

- Responses changed
  - New response: 200

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
                  - New enum values: [marketplace_offering_merge_created marketplace_offering_merge_executed marketplace_offering_merge_failed marketplace_offering_merge_undone marketplace_offering_merge_verification_failed marketplace_provider_project_group_gid_updated marketplace_resource_api_key_requested marketplace_resource_api_key_paused marketplace_resource_api_key_resumed marketplace_resource_api_key_updated marketplace_resource_api_key_deleted marketplace_resource_api_key_failed marketplace_resource_plan_switched proposal_draft_carried_over proposal_decision_reopened proposal_rejected_at_round_completion round_closed round_decision_started round_evaluation_started round_results_published round_undecided_proposals_rejected resource_update_metadata_failed resource_update_metadata_scheduled resource_update_metadata_succeeded reviewer_workload_limit_overridden role_cloned role_concealed role_definition_created role_definition_deleted role_definition_updated role_disabled role_enabled role_revealed matrix_password_generated matrix_recovery_key_escrowed matrix_recovery_key_viewed matrix_encryption_reset_started passkey_registered passkey_renamed passkey_revoked passkey_revoked_by_staff passkey_authentication_succeeded passkey_authentication_failed event_consumer_registered_with_broad_credential]

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
                              - New enum values: [RESOURCE.SET_SLUG MATRIX_ROOM.CREATE PROPOSAL.UPDATE PROJECT.SET_SLUG CUSTOMER.VIEW_TEAM PROJECT.VIEW_TEAM]
            - Modified property: permission_map
              - AdditionalProperties changed
                - New enum values: [RESOURCE.SET_SLUG MATRIX_ROOM.CREATE PROPOSAL.UPDATE PROJECT.SET_SLUG CUSTOMER.VIEW_TEAM PROJECT.VIEW_TEAM]
            - Modified property: permissions
              - AdditionalProperties changed
                - New enum values: [RESOURCE.SET_SLUG MATRIX_ROOM.CREATE PROPOSAL.UPDATE PROJECT.SET_SLUG CUSTOMER.VIEW_TEAM PROJECT.VIEW_TEAM]
            - Modified property: roles
              - AdditionalProperties changed
                - New enum values: [PROPOSAL.ADMIN]

POST /api/onboarding-verifications/{uuid}/create_customer/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_service_provider_manager_only

GET /api/openportal-unmanaged-projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_metrics]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_metrics
              - Modified property: project_metadata
                - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
                - Items changed
                  - Properties changed
                    - New property: modified
              - Modified property: slug
                - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

POST /api/openportal-unmanaged-projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

GET /api/openportal-unmanaged-projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_metrics]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

PATCH /api/openportal-unmanaged-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

PUT /api/openportal-unmanaged-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

GET /api/openportal-unmanaged-projects/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source

HEAD /api/openportal-unmanaged-projects/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

POST /api/openportal-unmanaged-projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

POST /api/openportal-unmanaged-projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

GET /api/openportal-unmanaged-projects/{uuid}/stats/

- New query param: include_terminated
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Required changed
                  - New required property: limit_usage_terminated
                  - New required property: usage_terminated
                - Properties changed
                  - New property: limit_usage_terminated
                  - New property: usage_terminated

GET /api/openstack-backups/

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
                    - Modified property: subnet_cidr
                      - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
              - Modified property: instance_ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - New property: instance_count
                    - Modified property: subnet_cidr
                      - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: floating_ips
                      - Items changed
                        - Properties changed
                          - Modified property: subnet_cidr
                            - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - Modified property: security_groups
                            - Items changed
                              - Properties changed
                                - New property: instance_count
                          - Modified property: subnet_cidr
                            - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'

GET /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: instance_count
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: subnet_cidr
                          - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: instance_count
                        - Modified property: subnet_cidr
                          - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'

PATCH /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: instance_count
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: subnet_cidr
                          - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: instance_count
                        - Modified property: subnet_cidr
                          - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'

PUT /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: instance_count
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: subnet_cidr
                          - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: instance_count
                        - Modified property: subnet_cidr
                          - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'

POST /api/openstack-backups/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: metadata
            - Modified property: availability_zone_name
              - Nullable changed from false to true
            - Modified property: floating_ips
              - ReadOnly changed from false to true
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: instance_count
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: type_name
                    - Nullable changed from false to true

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
                    - Modified property: cidr
                      - MaxLength changed from 32 to 43

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
                  - Modified property: cidr
                    - MaxLength changed from 32 to 43

GET /api/openstack-instances/

- New query param: security_group
- New query param: security_group_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [metadata]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: metadata
              - Modified property: availability_zone_name
                - Nullable changed from false to true
              - Modified property: floating_ips
                - ReadOnly changed from false to true
                - Items changed
                  - Properties changed
                    - Modified property: subnet_cidr
                      - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - New property: instance_count
                    - Modified property: subnet_cidr
                      - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
              - Modified property: volumes
                - Items changed
                  - Properties changed
                    - Modified property: type_name
                      - Nullable changed from false to true

HEAD /api/openstack-instances/

- New query param: security_group
- New query param: security_group_uuid

GET /api/openstack-instances/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [metadata]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: metadata
            - Modified property: availability_zone_name
              - Nullable changed from false to true
            - Modified property: floating_ips
              - ReadOnly changed from false to true
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: instance_count
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: type_name
                    - Nullable changed from false to true

PATCH /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: metadata
            - Modified property: availability_zone_name
              - Nullable changed from false to true
            - Modified property: floating_ips
              - ReadOnly changed from false to true
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: instance_count
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: type_name
                    - Nullable changed from false to true

PUT /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: metadata
            - Modified property: availability_zone_name
              - Nullable changed from false to true
            - Modified property: floating_ips
              - ReadOnly changed from false to true
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: instance_count
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: type_name
                    - Nullable changed from false to true

POST /api/openstack-instances/{uuid}/backup/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: instance_count
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: subnet_cidr
                          - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: instance_count
                        - Modified property: subnet_cidr
                          - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'

GET /api/openstack-instances/{uuid}/floating_ips/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: subnet_cidr
                - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'

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
                    - New property: instance_count
              - Modified property: subnet_cidr
                - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'

POST /api/openstack-loadbalancers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: vip_address
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: vip_address

GET /api/openstack-networks/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [tenant_is_managed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: tenant_is_managed
              - Modified property: subnets
                - Items changed
                  - Properties changed
                    - New property: ipv6_address_mode
                    - New property: ipv6_ra_mode
                    - Modified property: cidr
                      - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
                      - MaxLength changed from 32 to 43

GET /api/openstack-networks/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [tenant_is_managed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: tenant_is_managed
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - New property: ipv6_address_mode
                  - New property: ipv6_ra_mode
                  - Modified property: cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
                    - MaxLength changed from 32 to 43

PATCH /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: tenant_is_managed
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - New property: ipv6_address_mode
                  - New property: ipv6_ra_mode
                  - Modified property: cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
                    - MaxLength changed from 32 to 43

PUT /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: tenant_is_managed
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - New property: ipv6_address_mode
                  - New property: ipv6_ra_mode
                  - Modified property: cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
                    - MaxLength changed from 32 to 43

POST /api/openstack-networks/{uuid}/create_subnet/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ipv6_address_mode
          - New property: ipv6_ra_mode
          - New property: router
          - New property: skip_router_connection
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ipv6_address_mode
            - New property: ipv6_ra_mode
            - New property: router
            - New property: router_name
            - New property: router_uuid
            - New property: tenant_is_managed

GET /api/openstack-ports/

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
                    - Modified property: name
                      - ReadOnly changed from false to true
                      - MaxLength changed from 150 to null
                    - Modified property: url
                      - ReadOnly changed from true to false

POST /api/openstack-ports/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: security_groups
            - Items changed
              - Required changed
                - New required property: url
                - Deleted required property: name
              - Properties changed
                - New property: url
                - Deleted property: name
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: name
                    - ReadOnly changed from false to true
                    - MaxLength changed from 150 to null
                  - Modified property: url
                    - ReadOnly changed from true to false

GET /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: name
                    - ReadOnly changed from false to true
                    - MaxLength changed from 150 to null
                  - Modified property: url
                    - ReadOnly changed from true to false

PATCH /api/openstack-ports/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: security_groups
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: name
                    - ReadOnly changed from false to true
                    - MaxLength changed from 150 to null
                  - Modified property: url
                    - ReadOnly changed from true to false

PUT /api/openstack-ports/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: security_groups
            - Items changed
              - Required changed
                - New required property: url
                - Deleted required property: name
              - Properties changed
                - New property: url
                - Deleted property: name
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: name
                    - ReadOnly changed from false to true
                    - MaxLength changed from 150 to null
                  - Modified property: url
                    - ReadOnly changed from true to false

POST /api/openstack-ports/{uuid}/set_allowed_address_pairs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: name
                    - ReadOnly changed from false to true
                    - MaxLength changed from 150 to null
                  - Modified property: url
                    - ReadOnly changed from true to false

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
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - New property: instance_count
                    - Modified property: subnet_cidr
                      - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'

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
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: instance_count
                  - Modified property: subnet_cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'

GET /api/openstack-security-groups/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [instance_count]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: instance_count

GET /api/openstack-security-groups/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [instance_count]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: instance_count

POST /api/openstack-snapshots/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: availability_zone_name
              - Nullable changed from false to true
            - Modified property: type_name
              - Nullable changed from false to true

GET /api/openstack-subnets/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [ipv6_address_mode ipv6_ra_mode router router_name router_uuid skip_router_connection tenant_is_managed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: ipv6_address_mode
              - New property: ipv6_ra_mode
              - New property: router
              - New property: router_name
              - New property: router_uuid
              - New property: tenant_is_managed

GET /api/openstack-subnets/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [ipv6_address_mode ipv6_ra_mode router router_name router_uuid skip_router_connection tenant_is_managed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ipv6_address_mode
            - New property: ipv6_ra_mode
            - New property: router
            - New property: router_name
            - New property: router_uuid
            - New property: tenant_is_managed

PATCH /api/openstack-subnets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ipv6_address_mode
          - New property: ipv6_ra_mode
          - New property: router
          - New property: skip_router_connection
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ipv6_address_mode
            - New property: ipv6_ra_mode
            - New property: router
            - New property: router_name
            - New property: router_uuid
            - New property: tenant_is_managed

PUT /api/openstack-subnets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ipv6_address_mode
          - New property: ipv6_ra_mode
          - New property: router
          - New property: skip_router_connection
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ipv6_address_mode
            - New property: ipv6_ra_mode
            - New property: router
            - New property: router_name
            - New property: router_uuid
            - New property: tenant_is_managed

POST /api/openstack-subnets/{uuid}/connect/

- Description changed from 'Connect the subnet to the default tenant router.' to 'Connect the subnet to its router: the one chosen when the subnet was created or last attached to, and otherwise the tenant router Waldur picks.'

POST /api/openstack-subnets/{uuid}/disconnect/

- Description changed from 'Disconnect the subnet from the default tenant router.' to 'Disconnect the subnet from its router. The router is remembered, so connecting again returns the subnet to it.'

GET /api/openstack-tenants/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_managed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: is_managed

GET /api/openstack-tenants/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_managed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_managed

PATCH /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_managed

PUT /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_managed

POST /api/openstack-tenants/{uuid}/create_network/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: tenant_is_managed
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - New property: ipv6_address_mode
                  - New property: ipv6_ra_mode
                  - Modified property: cidr
                    - Description changed from 'IPv4 network address in CIDR format (e.g. 192.168.0.0/24)' to 'Network address in CIDR format (e.g. 192.168.0.0/24 or 2001:db8::/64)'
                    - MaxLength changed from 32 to 43

POST /api/openstack-tenants/{uuid}/create_security_group/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: instance_count

GET /api/openstack-volumes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: availability_zone_name
                - Nullable changed from false to true
              - Modified property: type_name
                - Nullable changed from false to true

GET /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: availability_zone_name
              - Nullable changed from false to true
            - Modified property: type_name
              - Nullable changed from false to true

PATCH /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: availability_zone_name
              - Nullable changed from false to true
            - Modified property: type_name
              - Nullable changed from false to true

PUT /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: availability_zone_name
              - Nullable changed from false to true
            - Modified property: type_name
              - Nullable changed from false to true

GET /api/override-settings/

- Description changed from 'Returns all settings that can be overridden in the database via the Constance backend. Requires admin permissions.' to 'Returns all settings that can be overridden in the database via the Constance backend. Staff receive every value. Support users receive the same keys, with secret_field values blanked.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ABOUT_US_PAGE_CONTENT
            - New property: ABOUT_US_PAGE_ENABLED
            - New property: ATLASSIAN_OAUTH2_CLIENT_SECRET
            - New property: DEFAULT_PROPOSAL_HIDDEN_FIELDS
            - New property: DEFAULT_PROPOSAL_REQUIRED_FIELDS
            - New property: MATRIX_AUTO_CREATE_PROJECT_ROOMS
            - New property: MATRIX_EXTERNAL_LOGIN_METHOD
            - New property: MATRIX_HISTORY_EXPORT_RETENTION_DAYS
            - New property: MATRIX_LIVEKIT_PUBLIC_URL
            - New property: MATRIX_SSO_REGISTRATION_METHOD
            - New property: MATRIX_TOKENS_MANAGED_BY
            - New property: METRICS_ARCHIVE_GRACE_DAYS
            - New property: METRICS_DEFAULT_RETENTION_POLICY
            - New property: METRICS_LATE_DATA_DAYS
            - New property: METRICS_MAX_OTLP_BODY_BYTES
            - New property: METRICS_MAX_POINTS_PER_REQUEST
            - New property: METRICS_MAX_SERIES_PER_RESOURCE_METRIC
            - New property: OIDC_REGISTRATION_METHOD
            - New property: PROPOSAL_DASHBOARD_REVIEWS_DUE_WITHIN_DAYS
            - New property: SCIM_USER_MATCH_SCIM_ATTRIBUTE
            - New property: SCIM_USER_MATCH_WALDUR_ATTRIBUTE
            - New property: SRAM_INTEGRATION_ENABLED
            - New property: SRAM_PLACEHOLDER_ROLE_TEMPLATE
            - New property: TELEMETRY_DEPLOYMENT_ID
            - New property: WALDUR_SUPPORT_ISSUE_KEY_PREFIX
            - Deleted property: MATRIX_LOGIN_METHOD
            - Deleted property: MATRIX_OIDC_PROVIDER_URL
            - Modified property: DISABLED_OFFERING_TYPES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/OfferingTypeEnum
                    - Deleted enum values: [SlurmInvoices.SlurmPackage]
            - Modified property: ENABLED_REPORTING_SCREENS
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/ENABLEDREPORTINGSCREENSEnum
                    - New enum values: [projects-by-affiliated-organization]
            - Modified property: ONBOARDING_VALIDATION_METHODS
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/OnboardingValidationEnum
                    - New enum values: [breg]

POST /api/override-settings/

- Description changed from 'Updates one or more settings in the database via the Constance backend. Requires admin permissions.' to 'Updates one or more settings in the database via the Constance backend. Requires staff permissions. Support users cannot update settings.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ABOUT_US_PAGE_CONTENT
          - New property: ABOUT_US_PAGE_ENABLED
          - New property: ATLASSIAN_OAUTH2_CLIENT_SECRET
          - New property: DEFAULT_PROPOSAL_HIDDEN_FIELDS
          - New property: DEFAULT_PROPOSAL_REQUIRED_FIELDS
          - New property: MATRIX_AUTO_CREATE_PROJECT_ROOMS
          - New property: MATRIX_EXTERNAL_LOGIN_METHOD
          - New property: MATRIX_HISTORY_EXPORT_RETENTION_DAYS
          - New property: MATRIX_LIVEKIT_PUBLIC_URL
          - New property: MATRIX_SSO_REGISTRATION_METHOD
          - New property: MATRIX_TOKENS_MANAGED_BY
          - New property: METRICS_ARCHIVE_GRACE_DAYS
          - New property: METRICS_DEFAULT_RETENTION_POLICY
          - New property: METRICS_LATE_DATA_DAYS
          - New property: METRICS_MAX_OTLP_BODY_BYTES
          - New property: METRICS_MAX_POINTS_PER_REQUEST
          - New property: METRICS_MAX_SERIES_PER_RESOURCE_METRIC
          - New property: OIDC_REGISTRATION_METHOD
          - New property: PROPOSAL_DASHBOARD_REVIEWS_DUE_WITHIN_DAYS
          - New property: SCIM_USER_MATCH_SCIM_ATTRIBUTE
          - New property: SCIM_USER_MATCH_WALDUR_ATTRIBUTE
          - New property: SRAM_INTEGRATION_ENABLED
          - New property: SRAM_PLACEHOLDER_ROLE_TEMPLATE
          - New property: TELEMETRY_DEPLOYMENT_ID
          - New property: WALDUR_SUPPORT_ISSUE_KEY_PREFIX
          - Deleted property: MATRIX_LOGIN_METHOD
          - Deleted property: MATRIX_OIDC_PROVIDER_URL
          - Modified property: DISABLED_OFFERING_TYPES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OfferingTypeEnum
                  - Deleted enum values: [SlurmInvoices.SlurmPackage]
          - Modified property: ENABLED_REPORTING_SCREENS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/ENABLEDREPORTINGSCREENSEnum
                  - New enum values: [projects-by-affiliated-organization]
          - Modified property: ONBOARDING_VALIDATION_METHODS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OnboardingValidationEnum
                  - New enum values: [breg]
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: ABOUT_US_PAGE_CONTENT
          - New property: ABOUT_US_PAGE_ENABLED
          - New property: ATLASSIAN_OAUTH2_CLIENT_SECRET
          - New property: DEFAULT_PROPOSAL_HIDDEN_FIELDS
          - New property: DEFAULT_PROPOSAL_REQUIRED_FIELDS
          - New property: MATRIX_AUTO_CREATE_PROJECT_ROOMS
          - New property: MATRIX_EXTERNAL_LOGIN_METHOD
          - New property: MATRIX_HISTORY_EXPORT_RETENTION_DAYS
          - New property: MATRIX_LIVEKIT_PUBLIC_URL
          - New property: MATRIX_SSO_REGISTRATION_METHOD
          - New property: MATRIX_TOKENS_MANAGED_BY
          - New property: METRICS_ARCHIVE_GRACE_DAYS
          - New property: METRICS_DEFAULT_RETENTION_POLICY
          - New property: METRICS_LATE_DATA_DAYS
          - New property: METRICS_MAX_OTLP_BODY_BYTES
          - New property: METRICS_MAX_POINTS_PER_REQUEST
          - New property: METRICS_MAX_SERIES_PER_RESOURCE_METRIC
          - New property: OIDC_REGISTRATION_METHOD
          - New property: PROPOSAL_DASHBOARD_REVIEWS_DUE_WITHIN_DAYS
          - New property: SCIM_USER_MATCH_SCIM_ATTRIBUTE
          - New property: SCIM_USER_MATCH_WALDUR_ATTRIBUTE
          - New property: SRAM_INTEGRATION_ENABLED
          - New property: SRAM_PLACEHOLDER_ROLE_TEMPLATE
          - New property: TELEMETRY_DEPLOYMENT_ID
          - New property: WALDUR_SUPPORT_ISSUE_KEY_PREFIX
          - Deleted property: MATRIX_LOGIN_METHOD
          - Deleted property: MATRIX_OIDC_PROVIDER_URL
          - Modified property: DISABLED_OFFERING_TYPES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OfferingTypeEnum
                  - Deleted enum values: [SlurmInvoices.SlurmPackage]
          - Modified property: ENABLED_REPORTING_SCREENS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/ENABLEDREPORTINGSCREENSEnum
                  - New enum values: [projects-by-affiliated-organization]
          - Modified property: ONBOARDING_VALIDATION_METHODS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OnboardingValidationEnum
                  - New enum values: [breg]
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: ABOUT_US_PAGE_CONTENT
          - New property: ABOUT_US_PAGE_ENABLED
          - New property: ATLASSIAN_OAUTH2_CLIENT_SECRET
          - New property: DEFAULT_PROPOSAL_HIDDEN_FIELDS
          - New property: DEFAULT_PROPOSAL_REQUIRED_FIELDS
          - New property: MATRIX_AUTO_CREATE_PROJECT_ROOMS
          - New property: MATRIX_EXTERNAL_LOGIN_METHOD
          - New property: MATRIX_HISTORY_EXPORT_RETENTION_DAYS
          - New property: MATRIX_LIVEKIT_PUBLIC_URL
          - New property: MATRIX_SSO_REGISTRATION_METHOD
          - New property: MATRIX_TOKENS_MANAGED_BY
          - New property: METRICS_ARCHIVE_GRACE_DAYS
          - New property: METRICS_DEFAULT_RETENTION_POLICY
          - New property: METRICS_LATE_DATA_DAYS
          - New property: METRICS_MAX_OTLP_BODY_BYTES
          - New property: METRICS_MAX_POINTS_PER_REQUEST
          - New property: METRICS_MAX_SERIES_PER_RESOURCE_METRIC
          - New property: OIDC_REGISTRATION_METHOD
          - New property: PROPOSAL_DASHBOARD_REVIEWS_DUE_WITHIN_DAYS
          - New property: SCIM_USER_MATCH_SCIM_ATTRIBUTE
          - New property: SCIM_USER_MATCH_WALDUR_ATTRIBUTE
          - New property: SRAM_INTEGRATION_ENABLED
          - New property: SRAM_PLACEHOLDER_ROLE_TEMPLATE
          - New property: TELEMETRY_DEPLOYMENT_ID
          - New property: WALDUR_SUPPORT_ISSUE_KEY_PREFIX
          - Deleted property: MATRIX_LOGIN_METHOD
          - Deleted property: MATRIX_OIDC_PROVIDER_URL
          - Modified property: DISABLED_OFFERING_TYPES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OfferingTypeEnum
                  - Deleted enum values: [SlurmInvoices.SlurmPackage]
          - Modified property: ENABLED_REPORTING_SCREENS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/ENABLEDREPORTINGSCREENSEnum
                  - New enum values: [projects-by-affiliated-organization]
          - Modified property: ONBOARDING_VALIDATION_METHODS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OnboardingValidationEnum
                  - New enum values: [breg]

GET /api/project-credits/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: creditable_cost_this_month
            - Properties changed
              - New property: creditable_cost_this_month

POST /api/project-credits/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: creditable_cost_this_month
          - Properties changed
            - New property: creditable_cost_this_month

GET /api/project-credits/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: creditable_cost_this_month
          - Properties changed
            - New property: creditable_cost_this_month

PATCH /api/project-credits/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: creditable_cost_this_month
          - Properties changed
            - New property: creditable_cost_this_month

PUT /api/project-credits/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: creditable_cost_this_month
          - Properties changed
            - New property: creditable_cost_this_month

GET /api/project-quotas/

- New query param: customer_uuid

HEAD /api/project-quotas/

- New query param: customer_uuid

GET /api/projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_metrics]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_metrics
              - Modified property: project_metadata
                - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
                - Items changed
                  - Properties changed
                    - New property: modified
              - Modified property: slug
                - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

POST /api/projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

GET /api/projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_metrics]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: slug
            - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

GET /api/projects/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source

HEAD /api/projects/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

POST /api/projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_metrics
            - Modified property: project_metadata
              - Description changed from 'Answers to the customer's project-metadata checklist (read-only).' to 'Answers to the customer's project-metadata checklist (read-only): the latest answer per question.'
              - Items changed
                - Properties changed
                  - New property: modified
            - Modified property: slug
              - Description changed from 'URL-friendly identifier. Only editable by staff users.' to 'URL-friendly identifier. Editable by staff; on create also by holders of PROJECT.SET_SLUG on the organization, otherwise ignored.'

GET /api/projects/{uuid}/stats/

- New query param: include_terminated
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Required changed
                  - New required property: limit_usage_terminated
                  - New required property: usage_terminated
                - Properties changed
                  - New property: limit_usage_terminated
                  - New property: usage_terminated

DELETE /api/promotions-campaigns/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'service_provider'

PUT /api/promotions-campaigns/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'service_provider'

POST /api/promotions-campaigns/{uuid}/activate/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'service_provider'

GET /api/promotions-campaigns/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [new_plan_billing_mode old_plan_billing_mode resource_end_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: new_plan_billing_mode
              - New property: old_plan_billing_mode
              - New property: resource_end_date
              - Modified property: limits
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: old_cost_estimate
                - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

GET /api/promotions-campaigns/{uuid}/resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_account_settings project_start_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_account_settings
              - New property: project_start_date
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: new_plan_billing_mode
                      - New property: old_plan_billing_mode
                      - New property: resource_end_date
                      - Modified property: limits
                        - AdditionalProperties changed
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                      - Modified property: old_cost_estimate
                        - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'
              - Modified property: is_limit_based
                - Description changed from 'Returns True if the resource has limit-based components with user-adjustable quotas.' to 'Returns True if the resource bills any component on user-adjustable limits under its plan.'
              - Modified property: is_usage_based
                - Description changed from 'Returns True if the resource has usage-based components that track variable consumption.' to 'Returns True if the resource bills any component by usage under its plan.'
              - Modified property: limits
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: new_plan_billing_mode
                      - New property: old_plan_billing_mode
                      - New property: resource_end_date
                      - Modified property: limits
                        - AdditionalProperties changed
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                      - Modified property: old_cost_estimate
                        - Description changed from '' to 'The old-limits estimate, snapshotted by init_cost() at creation.

Must not recompute live: _compute_old_cost_estimate() prices from
"today", which keeps advancing on every read while `cost` stays fixed
from creation -- the shown cost change would grow the longer an order
sits unread. Orders that predate this field have no snapshot, so they
fall back to the live computation rather than a wrong zero.'

POST /api/promotions-campaigns/{uuid}/terminate/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'service_provider'

GET /api/proposal-proposals/

- New query param: as_role
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: decision_held
            - Properties changed
              - New property: decision_held
              - Deleted property: duration_in_days
              - Deleted property: project_has_civilian_purpose
              - Deleted property: project_is_confidential
              - Modified property: round
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRound
                    - Properties changed
                      - New property: closed_at
                      - New property: deciding_started_at
                      - New property: evaluation_started_at
                      - New property: lifecycle_state
                      - New property: results_published_at

HEAD /api/proposal-proposals/

- New query param: as_role

POST /api/proposal-proposals/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: duration_in_days
          - Deleted property: project_has_civilian_purpose
          - Deleted property: project_is_confidential
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: decision_held
          - Properties changed
            - New property: decision_held
            - Deleted property: duration_in_days
            - Deleted property: project_has_civilian_purpose
            - Deleted property: project_is_confidential
            - Modified property: round
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRound
                  - Properties changed
                    - New property: closed_at
                    - New property: deciding_started_at
                    - New property: evaluation_started_at
                    - New property: lifecycle_state
                    - New property: results_published_at

GET /api/proposal-proposals/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: decision_held
          - Properties changed
            - New property: decision_held
            - Deleted property: duration_in_days
            - Deleted property: project_has_civilian_purpose
            - Deleted property: project_is_confidential
            - Modified property: round
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRound
                  - Properties changed
                    - New property: closed_at
                    - New property: deciding_started_at
                    - New property: evaluation_started_at
                    - New property: lifecycle_state
                    - New property: results_published_at

GET /api/proposal-proposals/{uuid}/completion_status/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/permission from 'PROPOSAL.MANAGE' to 'PROPOSAL.UPDATE'

GET /api/proposal-proposals/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source

HEAD /api/proposal-proposals/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

GET /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: limits
                - AdditionalProperties changed from true to null
                - AdditionalProperties changed
                  - Schema added
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: limit_decimal_places
                            - Modified property: default_limit
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'
                              - ExclusiveMin changed from null to true
                              - ExclusiveMax changed from null to true
                              - Min changed from -2.147483648e+09 to -1e+18
                              - Max changed from 2.147483647e+09 to 1e+18
                            - Modified property: is_builtin
                              - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                            - Modified property: limit_amount
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'
                              - ExclusiveMin changed from null to true
                              - ExclusiveMax changed from null to true
                              - Min changed from -2.147483648e+09 to -1e+18
                              - Max changed from 2.147483647e+09 to 1e+18
                            - Modified property: max_available_limit
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'
                              - ExclusiveMin changed from null to true
                              - ExclusiveMax changed from null to true
                              - Min changed from -2.147483648e+09 to -1e+18
                              - Max changed from 2.147483647e+09 to 1e+18
                            - Modified property: max_value
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'
                              - ExclusiveMin changed from null to true
                              - ExclusiveMax changed from null to true
                              - Min changed from -2.147483648e+09 to -1e+18
                              - Max changed from 2.147483647e+09 to 1e+18
                            - Modified property: min_value
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'
                              - ExclusiveMin changed from null to true
                              - ExclusiveMax changed from null to true
                              - Min changed from -2.147483648e+09 to -1e+18
                              - Max changed from 2.147483647e+09 to 1e+18
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - New property: component_formula_config
                                    - New property: component_sum_config
                                    - New property: pattern
                                    - New property: pattern_error
                                    - New property: unique
                                    - New property: visible_if
                                    - Modified property: default_configs
                                      - Properties changed
                                        - New property: load_balancer_mode
                                        - New property: topology_mode
                                    - Modified property: type
                                      - New enum values: [component_formula component_sum]
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - New property: billing_mode
                              - Modified property: components
                                - Items changed
                                  - Properties changed
                                    - New property: billing_type
                                    - New property: is_prepaid
                                    - New property: limit_period
                                    - Modified property: measured_unit
                                      - Description changed from 'Unit of measurement, for example, GB.' to ''
                                      - Nullable changed from false to true

POST /api/proposal-proposals/{uuid}/resources/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed from true to null
            - AdditionalProperties changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed from true to null
              - AdditionalProperties changed
                - Schema added
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: limit_decimal_places
                          - Modified property: default_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: is_builtin
                            - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                          - Modified property: limit_amount
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_available_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: min_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: component_formula_config
                                  - New property: component_sum_config
                                  - New property: pattern
                                  - New property: pattern_error
                                  - New property: unique
                                  - New property: visible_if
                                  - Modified property: default_configs
                                    - Properties changed
                                      - New property: load_balancer_mode
                                      - New property: topology_mode
                                  - Modified property: type
                                    - New enum values: [component_formula component_sum]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: billing_mode
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: billing_type
                                  - New property: is_prepaid
                                  - New property: limit_period
                                  - Modified property: measured_unit
                                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                                    - Nullable changed from false to true

DELETE /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed from true to null
              - AdditionalProperties changed
                - Schema added
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: limit_decimal_places
                          - Modified property: default_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: is_builtin
                            - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                          - Modified property: limit_amount
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_available_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: min_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: component_formula_config
                                  - New property: component_sum_config
                                  - New property: pattern
                                  - New property: pattern_error
                                  - New property: unique
                                  - New property: visible_if
                                  - Modified property: default_configs
                                    - Properties changed
                                      - New property: load_balancer_mode
                                      - New property: topology_mode
                                  - Modified property: type
                                    - New enum values: [component_formula component_sum]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: billing_mode
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: billing_type
                                  - New property: is_prepaid
                                  - New property: limit_period
                                  - Modified property: measured_unit
                                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                                    - Nullable changed from false to true

GET /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed from true to null
              - AdditionalProperties changed
                - Schema added
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: limit_decimal_places
                          - Modified property: default_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: is_builtin
                            - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                          - Modified property: limit_amount
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_available_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: min_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: component_formula_config
                                  - New property: component_sum_config
                                  - New property: pattern
                                  - New property: pattern_error
                                  - New property: unique
                                  - New property: visible_if
                                  - Modified property: default_configs
                                    - Properties changed
                                      - New property: load_balancer_mode
                                      - New property: topology_mode
                                  - Modified property: type
                                    - New enum values: [component_formula component_sum]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: billing_mode
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: billing_type
                                  - New property: is_prepaid
                                  - New property: limit_period
                                  - Modified property: measured_unit
                                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                                    - Nullable changed from false to true

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed from true to null
            - AdditionalProperties changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed from true to null
              - AdditionalProperties changed
                - Schema added
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: limit_decimal_places
                          - Modified property: default_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: is_builtin
                            - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                          - Modified property: limit_amount
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_available_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: min_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: component_formula_config
                                  - New property: component_sum_config
                                  - New property: pattern
                                  - New property: pattern_error
                                  - New property: unique
                                  - New property: visible_if
                                  - Modified property: default_configs
                                    - Properties changed
                                      - New property: load_balancer_mode
                                      - New property: topology_mode
                                  - Modified property: type
                                    - New enum values: [component_formula component_sum]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: billing_mode
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: billing_type
                                  - New property: is_prepaid
                                  - New property: limit_period
                                  - Modified property: measured_unit
                                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                                    - Nullable changed from false to true

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed from true to null
            - AdditionalProperties changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed from true to null
              - AdditionalProperties changed
                - Schema added
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: limit_decimal_places
                          - Modified property: default_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: is_builtin
                            - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                          - Modified property: limit_amount
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_available_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: min_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: component_formula_config
                                  - New property: component_sum_config
                                  - New property: pattern
                                  - New property: pattern_error
                                  - New property: unique
                                  - New property: visible_if
                                  - Modified property: default_configs
                                    - Properties changed
                                      - New property: load_balancer_mode
                                      - New property: topology_mode
                                  - Modified property: type
                                    - New enum values: [component_formula component_sum]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: billing_mode
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: billing_type
                                  - New property: is_prepaid
                                  - New property: limit_period
                                  - Modified property: measured_unit
                                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                                    - Nullable changed from false to true

GET /api/proposal-proposals/{uuid}/step-checklist-responses/

- New query param: as_role

POST /api/proposal-proposals/{uuid}/submit_answers/

- Extensions changed
  - Deleted extension: x-permissions

POST /api/proposal-proposals/{uuid}/update_project_details/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
          - Deleted property: duration_in_days
          - Deleted property: oecd_fos_2007_code
          - Deleted property: project_has_civilian_purpose
          - Deleted property: project_is_confidential

GET /api/proposal-proposals/{uuid}/workflow_states/

- New query param: as_role

GET /api/proposal-protected-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [carry_over_drafts evaluation_start max_prepaid_duration_months order_author order_author_user order_author_user_name order_author_user_uuid panel_chair panel_chair_name panel_chair_uuid proposal_field_config proposal_field_metadata publish_results undecided_at_round_completion]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: carry_over_drafts
              - New property: evaluation_start
              - New property: max_prepaid_duration_months
              - New property: order_author
              - New property: order_author_user
              - New property: order_author_user_name
              - New property: order_author_user_uuid
              - New property: panel_chair
              - New property: panel_chair_name
              - New property: panel_chair_uuid
              - New property: proposal_field_config
              - New property: proposal_field_metadata
              - New property: publish_results
              - New property: undecided_at_round_completion
              - Modified property: fixed_duration_in_days
                - Min changed from null to 1
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: limit_decimal_places
                          - Modified property: default_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: is_builtin
                            - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                          - Modified property: limit_amount
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_available_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: min_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: component_formula_config
                                  - New property: component_sum_config
                                  - New property: pattern
                                  - New property: pattern_error
                                  - New property: unique
                                  - New property: visible_if
                                  - Modified property: default_configs
                                    - Properties changed
                                      - New property: load_balancer_mode
                                      - New property: topology_mode
                                  - Modified property: type
                                    - New enum values: [component_formula component_sum]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: billing_mode
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: billing_type
                                  - New property: is_prepaid
                                  - New property: limit_period
                                  - Modified property: measured_unit
                                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                                    - Nullable changed from false to true
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: requested_offering_components
                      - Items changed
                        - Properties changed
                          - New property: limit_decimal_places
                          - Modified property: default_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: is_builtin
                            - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                          - Modified property: limit_amount
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_available_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: min_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: billing_mode
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: billing_type
                                  - New property: is_prepaid
                                  - New property: limit_period
                                  - Modified property: measured_unit
                                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                                    - Nullable changed from false to true
              - Modified property: rounds
                - Items changed
                  - Properties changed
                    - New property: closed_at
                    - New property: deciding_started_at
                    - New property: evaluation_started_at
                    - New property: lifecycle_state
                    - New property: results_published_at

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: carry_over_drafts
          - New property: evaluation_start
          - New property: order_author
          - New property: order_author_user
          - New property: panel_chair
          - New property: proposal_field_config
          - New property: publish_results
          - New property: undecided_at_round_completion
          - Modified property: fixed_duration_in_days
            - Min changed from null to 1
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: carry_over_drafts
            - New property: evaluation_start
            - New property: max_prepaid_duration_months
            - New property: order_author
            - New property: order_author_user
            - New property: order_author_user_name
            - New property: order_author_user_uuid
            - New property: panel_chair
            - New property: panel_chair_name
            - New property: panel_chair_uuid
            - New property: proposal_field_config
            - New property: proposal_field_metadata
            - New property: publish_results
            - New property: undecided_at_round_completion
            - Modified property: fixed_duration_in_days
              - Min changed from null to 1
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: component_formula_config
                                - New property: component_sum_config
                                - New property: pattern
                                - New property: pattern_error
                                - New property: unique
                                - New property: visible_if
                                - Modified property: default_configs
                                  - Properties changed
                                    - New property: load_balancer_mode
                                    - New property: topology_mode
                                - Modified property: type
                                  - New enum values: [component_formula component_sum]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: limits
                    - AdditionalProperties changed
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: closed_at
                  - New property: deciding_started_at
                  - New property: evaluation_started_at
                  - New property: lifecycle_state
                  - New property: results_published_at

GET /api/proposal-protected-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [carry_over_drafts evaluation_start max_prepaid_duration_months order_author order_author_user order_author_user_name order_author_user_uuid panel_chair panel_chair_name panel_chair_uuid proposal_field_config proposal_field_metadata publish_results undecided_at_round_completion]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: carry_over_drafts
            - New property: evaluation_start
            - New property: max_prepaid_duration_months
            - New property: order_author
            - New property: order_author_user
            - New property: order_author_user_name
            - New property: order_author_user_uuid
            - New property: panel_chair
            - New property: panel_chair_name
            - New property: panel_chair_uuid
            - New property: proposal_field_config
            - New property: proposal_field_metadata
            - New property: publish_results
            - New property: undecided_at_round_completion
            - Modified property: fixed_duration_in_days
              - Min changed from null to 1
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: component_formula_config
                                - New property: component_sum_config
                                - New property: pattern
                                - New property: pattern_error
                                - New property: unique
                                - New property: visible_if
                                - Modified property: default_configs
                                  - Properties changed
                                    - New property: load_balancer_mode
                                    - New property: topology_mode
                                - Modified property: type
                                  - New enum values: [component_formula component_sum]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: limits
                    - AdditionalProperties changed
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: closed_at
                  - New property: deciding_started_at
                  - New property: evaluation_started_at
                  - New property: lifecycle_state
                  - New property: results_published_at

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: carry_over_drafts
          - New property: evaluation_start
          - New property: order_author
          - New property: order_author_user
          - New property: panel_chair
          - New property: proposal_field_config
          - New property: publish_results
          - New property: undecided_at_round_completion
          - Modified property: fixed_duration_in_days
            - Min changed from null to 1
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: carry_over_drafts
            - New property: evaluation_start
            - New property: max_prepaid_duration_months
            - New property: order_author
            - New property: order_author_user
            - New property: order_author_user_name
            - New property: order_author_user_uuid
            - New property: panel_chair
            - New property: panel_chair_name
            - New property: panel_chair_uuid
            - New property: proposal_field_config
            - New property: proposal_field_metadata
            - New property: publish_results
            - New property: undecided_at_round_completion
            - Modified property: fixed_duration_in_days
              - Min changed from null to 1
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: component_formula_config
                                - New property: component_sum_config
                                - New property: pattern
                                - New property: pattern_error
                                - New property: unique
                                - New property: visible_if
                                - Modified property: default_configs
                                  - Properties changed
                                    - New property: load_balancer_mode
                                    - New property: topology_mode
                                - Modified property: type
                                  - New enum values: [component_formula component_sum]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: limits
                    - AdditionalProperties changed
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: closed_at
                  - New property: deciding_started_at
                  - New property: evaluation_started_at
                  - New property: lifecycle_state
                  - New property: results_published_at

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: carry_over_drafts
          - New property: evaluation_start
          - New property: order_author
          - New property: order_author_user
          - New property: panel_chair
          - New property: proposal_field_config
          - New property: publish_results
          - New property: undecided_at_round_completion
          - Modified property: fixed_duration_in_days
            - Min changed from null to 1
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: carry_over_drafts
            - New property: evaluation_start
            - New property: max_prepaid_duration_months
            - New property: order_author
            - New property: order_author_user
            - New property: order_author_user_name
            - New property: order_author_user_uuid
            - New property: panel_chair
            - New property: panel_chair_name
            - New property: panel_chair_uuid
            - New property: proposal_field_config
            - New property: proposal_field_metadata
            - New property: publish_results
            - New property: undecided_at_round_completion
            - Modified property: fixed_duration_in_days
              - Min changed from null to 1
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: component_formula_config
                                - New property: component_sum_config
                                - New property: pattern
                                - New property: pattern_error
                                - New property: unique
                                - New property: visible_if
                                - Modified property: default_configs
                                  - Properties changed
                                    - New property: load_balancer_mode
                                    - New property: topology_mode
                                - Modified property: type
                                  - New enum values: [component_formula component_sum]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: limits
                    - AdditionalProperties changed
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: closed_at
                  - New property: deciding_started_at
                  - New property: evaluation_started_at
                  - New property: lifecycle_state
                  - New property: results_published_at

GET /api/proposal-protected-calls/{uuid}/compliance_overview/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes from '<nil>' to '[* manager]'

GET /api/proposal-protected-calls/{uuid}/conflicts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: status
            - Properties changed
              - Modified property: status
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/ConflictOfInterestStatusEnum
                - Type changed from 'string' to ''
                - Deleted enum values: [pending dismissed waived recused]
                - ReadOnly changed from false to true

POST /api/proposal-protected-calls/{uuid}/create-manual-assignment/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: override_workload_limit

POST /api/proposal-protected-calls/{uuid}/duplicate/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: copy_proposal_field_config
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: carry_over_drafts
            - New property: evaluation_start
            - New property: max_prepaid_duration_months
            - New property: order_author
            - New property: order_author_user
            - New property: order_author_user_name
            - New property: order_author_user_uuid
            - New property: panel_chair
            - New property: panel_chair_name
            - New property: panel_chair_uuid
            - New property: proposal_field_config
            - New property: proposal_field_metadata
            - New property: publish_results
            - New property: undecided_at_round_completion
            - Modified property: fixed_duration_in_days
              - Min changed from null to 1
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: component_formula_config
                                - New property: component_sum_config
                                - New property: pattern
                                - New property: pattern_error
                                - New property: unique
                                - New property: visible_if
                                - Modified property: default_configs
                                  - Properties changed
                                    - New property: load_balancer_mode
                                    - New property: topology_mode
                                - Modified property: type
                                  - New enum values: [component_formula component_sum]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: limits
                    - AdditionalProperties changed
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: closed_at
                  - New property: deciding_started_at
                  - New property: evaluation_started_at
                  - New property: lifecycle_state
                  - New property: results_published_at

POST /api/proposal-protected-calls/{uuid}/invite-by-email/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_assignments
              - Description changed from '' to 'Number of the reviewer's open assignments in this call: pending or accepted assignment items whose review is not finished, plus reviews in progress created without an assignment item.'

GET /api/proposal-protected-calls/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source

HEAD /api/proposal-protected-calls/{uuid}/list_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [source]

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
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: component_formula_config
                            - New property: component_sum_config
                            - New property: pattern
                            - New property: pattern_error
                            - New property: unique
                            - New property: visible_if
                            - Modified property: default_configs
                              - Properties changed
                                - New property: load_balancer_mode
                                - New property: topology_mode
                            - Modified property: type
                              - New enum values: [component_formula component_sum]
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - New property: billing_mode
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: billing_type
                            - New property: is_prepaid
                            - New property: limit_period
                            - Modified property: measured_unit
                              - Description changed from 'Unit of measurement, for example, GB.' to ''
                              - Nullable changed from false to true

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
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

DELETE /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

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
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

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
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

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
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

GET /api/proposal-protected-calls/{uuid}/proposals/{proposal_uuid}/compliance-answers/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes from '<nil>' to '[* manager]'

GET /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: limits
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: requested_offering_components
                - Items changed
                  - Properties changed
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: requested_offering_plan
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - New property: billing_mode
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: billing_type
                            - New property: is_prepaid
                            - New property: limit_period
                            - Modified property: measured_unit
                              - Description changed from 'Unit of measurement, for example, GB.' to ''
                              - Nullable changed from false to true

POST /api/proposal-protected-calls/{uuid}/resource_templates/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: requested_offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

DELETE /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: requested_offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

GET /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: requested_offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

PATCH /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: requested_offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

PUT /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - AdditionalProperties changed
              - Type changed from 'integer' to 'number'
              - Format changed from '' to 'double'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: requested_offering_components
              - Items changed
                - Properties changed
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

POST /api/proposal-protected-calls/{uuid}/review_proposal_compliance/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes from '<nil>' to '[* manager]'

GET /api/proposal-protected-calls/{uuid}/reviewer-pool/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: current_assignments
                - Description changed from '' to 'Number of the reviewer's open assignments in this call: pending or accepted assignment items whose review is not finished, plus reviews in progress created without an assignment item.'

POST /api/proposal-protected-calls/{uuid}/reviewer-pool/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: current_assignments
                - Description changed from '' to 'Number of the reviewer's open assignments in this call: pending or accepted assignment items whose review is not finished, plus reviews in progress created without an assignment item.'

POST /api/proposal-protected-calls/{uuid}/rounds-bulk-set/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes from '<nil>' to '[* manager]'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: adopted_at
              - New required property: adoption_document
              - New required property: adoption_note
              - New required property: closed_at
              - New required property: deciding_started_at
              - New required property: evaluation_started_at
              - New required property: has_proposals
              - New required property: held_decisions_count
              - New required property: lifecycle_state
              - New required property: results_forced_reason
              - New required property: results_published_at
              - New required property: results_published_by_name
            - Properties changed
              - New property: adopted_at
              - New property: adoption_document
              - New property: adoption_note
              - New property: closed_at
              - New property: deciding_started_at
              - New property: evaluation_started_at
              - New property: has_proposals
              - New property: held_decisions_count
              - New property: lifecycle_state
              - New property: results_forced_reason
              - New property: results_published_at
              - New property: results_published_by_name
              - New property: undecided_at_round_completion

GET /api/proposal-protected-calls/{uuid}/rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: adopted_at
              - New required property: adoption_document
              - New required property: adoption_note
              - New required property: closed_at
              - New required property: deciding_started_at
              - New required property: evaluation_started_at
              - New required property: has_proposals
              - New required property: held_decisions_count
              - New required property: lifecycle_state
              - New required property: results_forced_reason
              - New required property: results_published_at
              - New required property: results_published_by_name
            - Properties changed
              - New property: adopted_at
              - New property: adoption_document
              - New property: adoption_note
              - New property: closed_at
              - New property: deciding_started_at
              - New property: evaluation_started_at
              - New property: has_proposals
              - New property: held_decisions_count
              - New property: lifecycle_state
              - New property: results_forced_reason
              - New property: results_published_at
              - New property: results_published_by_name
              - New property: undecided_at_round_completion

POST /api/proposal-protected-calls/{uuid}/rounds/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: undecided_at_round_completion
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: adopted_at
            - New required property: adoption_document
            - New required property: adoption_note
            - New required property: closed_at
            - New required property: deciding_started_at
            - New required property: evaluation_started_at
            - New required property: has_proposals
            - New required property: held_decisions_count
            - New required property: lifecycle_state
            - New required property: results_forced_reason
            - New required property: results_published_at
            - New required property: results_published_by_name
          - Properties changed
            - New property: adopted_at
            - New property: adoption_document
            - New property: adoption_note
            - New property: closed_at
            - New property: deciding_started_at
            - New property: evaluation_started_at
            - New property: has_proposals
            - New property: held_decisions_count
            - New property: lifecycle_state
            - New property: results_forced_reason
            - New property: results_published_at
            - New property: results_published_by_name
            - New property: undecided_at_round_completion

DELETE /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: adopted_at
            - New required property: adoption_document
            - New required property: adoption_note
            - New required property: closed_at
            - New required property: deciding_started_at
            - New required property: evaluation_started_at
            - New required property: has_proposals
            - New required property: held_decisions_count
            - New required property: lifecycle_state
            - New required property: results_forced_reason
            - New required property: results_published_at
            - New required property: results_published_by_name
          - Properties changed
            - New property: adopted_at
            - New property: adoption_document
            - New property: adoption_note
            - New property: closed_at
            - New property: deciding_started_at
            - New property: evaluation_started_at
            - New property: has_proposals
            - New property: held_decisions_count
            - New property: lifecycle_state
            - New property: results_forced_reason
            - New property: results_published_at
            - New property: results_published_by_name
            - New property: undecided_at_round_completion

GET /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: adopted_at
            - New required property: adoption_document
            - New required property: adoption_note
            - New required property: closed_at
            - New required property: deciding_started_at
            - New required property: evaluation_started_at
            - New required property: has_proposals
            - New required property: held_decisions_count
            - New required property: lifecycle_state
            - New required property: results_forced_reason
            - New required property: results_published_at
            - New required property: results_published_by_name
          - Properties changed
            - New property: adopted_at
            - New property: adoption_document
            - New property: adoption_note
            - New property: closed_at
            - New property: deciding_started_at
            - New property: evaluation_started_at
            - New property: has_proposals
            - New property: held_decisions_count
            - New property: lifecycle_state
            - New property: results_forced_reason
            - New property: results_published_at
            - New property: results_published_by_name
            - New property: undecided_at_round_completion

PATCH /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: undecided_at_round_completion
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: adopted_at
            - New required property: adoption_document
            - New required property: adoption_note
            - New required property: closed_at
            - New required property: deciding_started_at
            - New required property: evaluation_started_at
            - New required property: has_proposals
            - New required property: held_decisions_count
            - New required property: lifecycle_state
            - New required property: results_forced_reason
            - New required property: results_published_at
            - New required property: results_published_by_name
          - Properties changed
            - New property: adopted_at
            - New property: adoption_document
            - New property: adoption_note
            - New property: closed_at
            - New property: deciding_started_at
            - New property: evaluation_started_at
            - New property: has_proposals
            - New property: held_decisions_count
            - New property: lifecycle_state
            - New property: results_forced_reason
            - New property: results_published_at
            - New property: results_published_by_name
            - New property: undecided_at_round_completion

PUT /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: undecided_at_round_completion
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: adopted_at
            - New required property: adoption_document
            - New required property: adoption_note
            - New required property: closed_at
            - New required property: deciding_started_at
            - New required property: evaluation_started_at
            - New required property: has_proposals
            - New required property: held_decisions_count
            - New required property: lifecycle_state
            - New required property: results_forced_reason
            - New required property: results_published_at
            - New required property: results_published_by_name
          - Properties changed
            - New property: adopted_at
            - New property: adoption_document
            - New property: adoption_note
            - New property: closed_at
            - New property: deciding_started_at
            - New property: evaluation_started_at
            - New property: has_proposals
            - New property: held_decisions_count
            - New property: lifecycle_state
            - New property: results_forced_reason
            - New property: results_published_at
            - New property: results_published_by_name
            - New property: undecided_at_round_completion

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: carry_over_drafts
          - New property: evaluation_start
          - New property: order_author
          - New property: order_author_user
          - New property: panel_chair
          - New property: proposal_field_config
          - New property: publish_results
          - New property: undecided_at_round_completion
          - Modified property: fixed_duration_in_days
            - Min changed from null to 1

GET /api/proposal-protected-calls/{uuid}/workflow_steps/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: notification_rules
              - New required property: responsible_users
            - Properties changed
              - New property: notification_rules
              - New property: responsible_users

POST /api/proposal-protected-calls/{uuid}/workflow_steps/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: notification_rules
            - New required property: responsible_users
          - Properties changed
            - New property: notification_rules
            - New property: responsible_users

DELETE /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: notification_rules
            - New required property: responsible_users
          - Properties changed
            - New property: notification_rules
            - New property: responsible_users

GET /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: notification_rules
            - New required property: responsible_users
          - Properties changed
            - New property: notification_rules
            - New property: responsible_users

PATCH /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: notification_rules
            - New required property: responsible_users
          - Properties changed
            - New property: notification_rules
            - New property: responsible_users

PUT /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: notification_rules
            - New required property: responsible_users
          - Properties changed
            - New property: notification_rules
            - New property: responsible_users

GET /api/proposal-public-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [evaluation_start max_prepaid_duration_months proposal_field_config publish_results]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: evaluation_start
              - New property: max_prepaid_duration_months
              - New property: proposal_field_config
              - New property: publish_results
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: limit_decimal_places
                          - Modified property: default_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: is_builtin
                            - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                          - Modified property: limit_amount
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_available_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: min_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: component_formula_config
                                  - New property: component_sum_config
                                  - New property: pattern
                                  - New property: pattern_error
                                  - New property: unique
                                  - New property: visible_if
                                  - Modified property: default_configs
                                    - Properties changed
                                      - New property: load_balancer_mode
                                      - New property: topology_mode
                                  - Modified property: type
                                    - New enum values: [component_formula component_sum]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: billing_mode
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: billing_type
                                  - New property: is_prepaid
                                  - New property: limit_period
                                  - Modified property: measured_unit
                                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                                    - Nullable changed from false to true
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: limits
                      - AdditionalProperties changed
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'
                    - Modified property: requested_offering_components
                      - Items changed
                        - Properties changed
                          - New property: limit_decimal_places
                          - Modified property: default_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: is_builtin
                            - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                          - Modified property: limit_amount
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_available_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: min_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: billing_mode
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: billing_type
                                  - New property: is_prepaid
                                  - New property: limit_period
                                  - Modified property: measured_unit
                                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                                    - Nullable changed from false to true
              - Modified property: rounds
                - Items changed
                  - Properties changed
                    - New property: closed_at
                    - New property: deciding_started_at
                    - New property: evaluation_started_at
                    - New property: lifecycle_state
                    - New property: results_published_at

GET /api/proposal-public-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [evaluation_start max_prepaid_duration_months proposal_field_config publish_results]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: evaluation_start
            - New property: max_prepaid_duration_months
            - New property: proposal_field_config
            - New property: publish_results
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: component_formula_config
                                - New property: component_sum_config
                                - New property: pattern
                                - New property: pattern_error
                                - New property: unique
                                - New property: visible_if
                                - Modified property: default_configs
                                  - Properties changed
                                    - New property: load_balancer_mode
                                    - New property: topology_mode
                                - Modified property: type
                                  - New enum values: [component_formula component_sum]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: limits
                    - AdditionalProperties changed
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: limit_decimal_places
                        - Modified property: default_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: is_builtin
                          - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                        - Modified property: limit_amount
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_available_limit
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: max_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                        - Modified property: min_value
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'
                          - ExclusiveMin changed from null to true
                          - ExclusiveMax changed from null to true
                          - Min changed from -2.147483648e+09 to -1e+18
                          - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: billing_mode
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: billing_type
                                - New property: is_prepaid
                                - New property: limit_period
                                - Modified property: measured_unit
                                  - Description changed from 'Unit of measurement, for example, GB.' to ''
                                  - Nullable changed from false to true
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: closed_at
                  - New property: deciding_started_at
                  - New property: evaluation_started_at
                  - New property: lifecycle_state
                  - New property: results_published_at

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
                    - New property: limit_decimal_places
                    - Modified property: default_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: is_builtin
                      - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                    - Modified property: limit_amount
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_available_limit
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: max_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: min_value
                      - Type changed from 'integer' to 'number'
                      - Format changed from '' to 'double'
                      - ExclusiveMin changed from null to true
                      - ExclusiveMax changed from null to true
                      - Min changed from -2.147483648e+09 to -1e+18
                      - Max changed from 2.147483647e+09 to 1e+18
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: component_formula_config
                            - New property: component_sum_config
                            - New property: pattern
                            - New property: pattern_error
                            - New property: unique
                            - New property: visible_if
                            - Modified property: default_configs
                              - Properties changed
                                - New property: load_balancer_mode
                                - New property: topology_mode
                            - Modified property: type
                              - New enum values: [component_formula component_sum]
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - New property: billing_mode
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: billing_type
                            - New property: is_prepaid
                            - New property: limit_period
                            - Modified property: measured_unit
                              - Description changed from 'Unit of measurement, for example, GB.' to ''
                              - Nullable changed from false to true

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
                  - New property: limit_decimal_places
                  - Modified property: default_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: is_builtin
                    - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                  - Modified property: limit_amount
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_available_limit
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: max_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
                  - Modified property: min_value
                    - Type changed from 'integer' to 'number'
                    - Format changed from '' to 'double'
                    - ExclusiveMin changed from null to true
                    - ExclusiveMax changed from null to true
                    - Min changed from -2.147483648e+09 to -1e+18
                    - Max changed from 2.147483647e+09 to 1e+18
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: component_formula_config
                          - New property: component_sum_config
                          - New property: pattern
                          - New property: pattern_error
                          - New property: unique
                          - New property: visible_if
                          - Modified property: default_configs
                            - Properties changed
                              - New property: load_balancer_mode
                              - New property: topology_mode
                          - Modified property: type
                            - New enum values: [component_formula component_sum]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: billing_mode
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: billing_type
                          - New property: is_prepaid
                          - New property: limit_period
                          - Modified property: measured_unit
                            - Description changed from 'Unit of measurement, for example, GB.' to ''
                            - Nullable changed from false to true

GET /api/proposal-requested-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: limits
                - AdditionalProperties changed from true to null
                - AdditionalProperties changed
                  - Schema added
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: limit_decimal_places
                            - Modified property: default_limit
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'
                              - ExclusiveMin changed from null to true
                              - ExclusiveMax changed from null to true
                              - Min changed from -2.147483648e+09 to -1e+18
                              - Max changed from 2.147483647e+09 to 1e+18
                            - Modified property: is_builtin
                              - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                            - Modified property: limit_amount
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'
                              - ExclusiveMin changed from null to true
                              - ExclusiveMax changed from null to true
                              - Min changed from -2.147483648e+09 to -1e+18
                              - Max changed from 2.147483647e+09 to 1e+18
                            - Modified property: max_available_limit
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'
                              - ExclusiveMin changed from null to true
                              - ExclusiveMax changed from null to true
                              - Min changed from -2.147483648e+09 to -1e+18
                              - Max changed from 2.147483647e+09 to 1e+18
                            - Modified property: max_value
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'
                              - ExclusiveMin changed from null to true
                              - ExclusiveMax changed from null to true
                              - Min changed from -2.147483648e+09 to -1e+18
                              - Max changed from 2.147483647e+09 to 1e+18
                            - Modified property: min_value
                              - Type changed from 'integer' to 'number'
                              - Format changed from '' to 'double'
                              - ExclusiveMin changed from null to true
                              - ExclusiveMax changed from null to true
                              - Min changed from -2.147483648e+09 to -1e+18
                              - Max changed from 2.147483647e+09 to 1e+18
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - New property: component_formula_config
                                    - New property: component_sum_config
                                    - New property: pattern
                                    - New property: pattern_error
                                    - New property: unique
                                    - New property: visible_if
                                    - Modified property: default_configs
                                      - Properties changed
                                        - New property: load_balancer_mode
                                        - New property: topology_mode
                                    - Modified property: type
                                      - New enum values: [component_formula component_sum]
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - New property: billing_mode
                              - Modified property: components
                                - Items changed
                                  - Properties changed
                                    - New property: billing_type
                                    - New property: is_prepaid
                                    - New property: limit_period
                                    - Modified property: measured_unit
                                      - Description changed from 'Unit of measurement, for example, GB.' to ''
                                      - Nullable changed from false to true

GET /api/proposal-requested-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: limits
              - AdditionalProperties changed from true to null
              - AdditionalProperties changed
                - Schema added
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: limit_decimal_places
                          - Modified property: default_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: is_builtin
                            - Description changed from '' to 'The API's older name for ``billed_per_plan``.

It used to ask the plugin registry whether this component's type is one
the plugin declares, which left out the OpenStack per-volume-type
quotas: they are created by the volume type sync rather than declared,
so the API called them provider components while the billing resolver
treated them as builtin. Reading the stored flag makes the two agree.'
                          - Modified property: limit_amount
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_available_limit
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: max_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                          - Modified property: min_value
                            - Type changed from 'integer' to 'number'
                            - Format changed from '' to 'double'
                            - ExclusiveMin changed from null to true
                            - ExclusiveMax changed from null to true
                            - Min changed from -2.147483648e+09 to -1e+18
                            - Max changed from 2.147483647e+09 to 1e+18
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: component_formula_config
                                  - New property: component_sum_config
                                  - New property: pattern
                                  - New property: pattern_error
                                  - New property: unique
                                  - New property: visible_if
                                  - Modified property: default_configs
                                    - Properties changed
                                      - New property: load_balancer_mode
                                      - New property: topology_mode
                                  - Modified property: type
                                    - New enum values: [component_formula component_sum]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: billing_mode
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: billing_type
                                  - New property: is_prepaid
                                  - New property: limit_period
                                  - Modified property: measured_unit
                                    - Description changed from 'Unit of measurement, for example, GB.' to ''
                                    - Nullable changed from false to true

GET /api/proposal-reviews/

- New query param: due_within_days
- New query param: managed_calls_only
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: comment_project_duration
              - Deleted property: comment_project_has_civilian_purpose
              - Deleted property: comment_project_is_confidential
              - Modified property: review_end_date
                - Description changed from '' to 'When the review is due, or None if the round sets no review duration.

A review created by accepting an assignment is also due no earlier than
its assignment batch's deadline, so extending the batch deadline moves
the deadline of the reviews accepted from it.'
                - Nullable changed from false to true

HEAD /api/proposal-reviews/

- New query param: due_within_days
- New query param: managed_calls_only

POST /api/proposal-reviews/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: override_workload_limit
          - Deleted property: comment_project_duration
          - Deleted property: comment_project_has_civilian_purpose
          - Deleted property: comment_project_is_confidential
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: comment_project_duration
            - Deleted property: comment_project_has_civilian_purpose
            - Deleted property: comment_project_is_confidential
            - Modified property: review_end_date
              - Description changed from '' to 'When the review is due, or None if the round sets no review duration.

A review created by accepting an assignment is also due no earlier than
its assignment batch's deadline, so extending the batch deadline moves
the deadline of the reviews accepted from it.'
              - Nullable changed from false to true

GET /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: comment_project_duration
            - Deleted property: comment_project_has_civilian_purpose
            - Deleted property: comment_project_is_confidential
            - Modified property: review_end_date
              - Description changed from '' to 'When the review is due, or None if the round sets no review duration.

A review created by accepting an assignment is also due no earlier than
its assignment batch's deadline, so extending the batch deadline moves
the deadline of the reviews accepted from it.'
              - Nullable changed from false to true

PATCH /api/proposal-reviews/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: override_workload_limit
          - Deleted property: comment_project_duration
          - Deleted property: comment_project_has_civilian_purpose
          - Deleted property: comment_project_is_confidential
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: comment_project_duration
            - Deleted property: comment_project_has_civilian_purpose
            - Deleted property: comment_project_is_confidential
            - Modified property: review_end_date
              - Description changed from '' to 'When the review is due, or None if the round sets no review duration.

A review created by accepting an assignment is also due no earlier than
its assignment batch's deadline, so extending the batch deadline moves
the deadline of the reviews accepted from it.'
              - Nullable changed from false to true

PUT /api/proposal-reviews/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: override_workload_limit
          - Deleted property: comment_project_duration
          - Deleted property: comment_project_has_civilian_purpose
          - Deleted property: comment_project_is_confidential
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: comment_project_duration
            - Deleted property: comment_project_has_civilian_purpose
            - Deleted property: comment_project_is_confidential
            - Modified property: review_end_date
              - Description changed from '' to 'When the review is due, or None if the round sets no review duration.

A review created by accepting an assignment is also due no earlier than
its assignment batch's deadline, so extending the batch deadline moves
the deadline of the reviews accepted from it.'
              - Nullable changed from false to true

GET /api/provider-invoice-items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: details
                - Properties changed
                  - Modified property: resource_limit_periods
                    - Items changed
                      - Properties changed
                        - Modified property: quantity
                          - Type changed from 'integer' to 'number'
                          - Format changed from '' to 'double'

GET /api/provider-invoice-items/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: details
              - Properties changed
                - Modified property: resource_limit_periods
                  - Items changed
                    - Properties changed
                      - Modified property: quantity
                        - Type changed from 'integer' to 'number'
                        - Format changed from '' to 'double'

GET /api/provider-tickets/

- New query param: provider_helpdesk_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: provider_helpdesk_uuid
            - Properties changed
              - New property: provider_helpdesk_uuid

HEAD /api/provider-tickets/

- New query param: provider_helpdesk_uuid

GET /api/provider-tickets/stats/

- New query param: provider_helpdesk_uuid

HEAD /api/provider-tickets/stats/

- New query param: provider_helpdesk_uuid

GET /api/provider-tickets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: provider_helpdesk_uuid
          - Properties changed
            - New property: provider_helpdesk_uuid

PATCH /api/provider-tickets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: provider_helpdesk_uuid
          - Properties changed
            - New property: provider_helpdesk_uuid

PUT /api/provider-tickets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: provider_helpdesk_uuid
          - Properties changed
            - New property: provider_helpdesk_uuid

GET /api/rabbitmq-stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: vhosts
              - Items changed
                - Properties changed
                  - Modified property: queues
                    - Items changed
                      - Required changed
                        - New required property: consumer_uuid
                        - New required property: queue_kind
                      - Properties changed
                        - New property: consumer_uuid
                        - New property: queue_kind

GET /api/reviewer-invitations/{token}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: invited_at
          - Properties changed
            - New property: invited_at

GET /api/roles/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [description_hr]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: description_hr

POST /api/roles/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_hr
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_hr

GET /api/roles/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [description_hr]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_hr

PATCH /api/roles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_hr
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_hr

PUT /api/roles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_hr
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_hr

POST /api/roles/{uuid}/clone_to_customer/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_hr

PUT /api/roles/{uuid}/update_descriptions/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_hr
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_hr

GET /api/support-issues/

- New query param: is_open
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: available_statuses
            - Properties changed
              - New property: available_statuses

HEAD /api/support-issues/

- New query param: is_open

POST /api/support-issues/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: first_comment
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: available_statuses
          - Properties changed
            - New property: available_statuses

GET /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: available_statuses
          - Properties changed
            - New property: available_statuses

PATCH /api/support-issues/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: first_comment
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: available_statuses
          - Properties changed
            - New property: available_statuses

PUT /api/support-issues/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: first_comment
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: available_statuses
          - Properties changed
            - New property: available_statuses

POST /api/support-issues/{uuid}/attach_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: available_statuses
          - Properties changed
            - New property: available_statuses

POST /api/support-issues/{uuid}/reroute/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: available_statuses
          - Properties changed
            - New property: available_statuses

POST /api/support-issues/{uuid}/route_to_provider/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: available_statuses
          - Properties changed
            - New property: available_statuses

POST /api/support/settings/atlassian/discover_custom_fields/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: client_id
          - New property: client_secret
          - Modified property: api_url
            - Description changed from 'Atlassian API URL (e.g., <https://your-domain.atlassian.net>)' to 'Atlassian site or API URL (e.g., <https://your-domain.atlassian.net>). With OAuth 2.0 client credentials a Cloud site URL is resolved to the API gateway URL.'
          - Modified property: auth_method
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/AuthMethodEnum
                - New enum values: [oauth2_client_credentials]

POST /api/support/settings/atlassian/discover_priorities/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: client_id
          - New property: client_secret
          - Modified property: api_url
            - Description changed from 'Atlassian API URL (e.g., <https://your-domain.atlassian.net>)' to 'Atlassian site or API URL (e.g., <https://your-domain.atlassian.net>). With OAuth 2.0 client credentials a Cloud site URL is resolved to the API gateway URL.'
          - Modified property: auth_method
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/AuthMethodEnum
                - New enum values: [oauth2_client_credentials]

POST /api/support/settings/atlassian/discover_projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: client_id
          - New property: client_secret
          - Modified property: api_url
            - Description changed from 'Atlassian API URL (e.g., <https://your-domain.atlassian.net>)' to 'Atlassian site or API URL (e.g., <https://your-domain.atlassian.net>). With OAuth 2.0 client credentials a Cloud site URL is resolved to the API gateway URL.'
          - Modified property: auth_method
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/AuthMethodEnum
                - New enum values: [oauth2_client_credentials]

POST /api/support/settings/atlassian/discover_request_types/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: client_id
          - New property: client_secret
          - Modified property: api_url
            - Description changed from 'Atlassian API URL (e.g., <https://your-domain.atlassian.net>)' to 'Atlassian site or API URL (e.g., <https://your-domain.atlassian.net>). With OAuth 2.0 client credentials a Cloud site URL is resolved to the API gateway URL.'
          - Modified property: auth_method
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/AuthMethodEnum
                - New enum values: [oauth2_client_credentials]

POST /api/support/settings/atlassian/preview_settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: client_id
          - New property: client_secret
          - Modified property: api_url
            - Description changed from '' to 'Atlassian site or API URL (e.g., <https://your-domain.atlassian.net>). With OAuth 2.0 client credentials a Cloud site URL is resolved to the API gateway URL.'
          - Modified property: auth_method
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/AuthMethodEnum
            - Type changed from 'string' to ''
            - Description changed from '' to 'Authentication method to use'
            - Deleted enum values: [api_token personal_access_token basic]

POST /api/support/settings/atlassian/save_settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: client_id
          - New property: client_secret
          - Modified property: api_url
            - Description changed from '' to 'Atlassian site or API URL (e.g., <https://your-domain.atlassian.net>). With OAuth 2.0 client credentials a Cloud site URL is resolved to the API gateway URL.'
          - Modified property: auth_method
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/AuthMethodEnum
            - Type changed from 'string' to ''
            - Description changed from '' to 'Authentication method to use'
            - Deleted enum values: [api_token personal_access_token basic]

POST /api/support/settings/atlassian/validate_credentials/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: client_id
          - New property: client_secret
          - Modified property: api_url
            - Description changed from 'Atlassian API URL (e.g., <https://your-domain.atlassian.net>)' to 'Atlassian site or API URL (e.g., <https://your-domain.atlassian.net>). With OAuth 2.0 client credentials a Cloud site URL is resolved to the API gateway URL.'
          - Modified property: auth_method
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/AuthMethodEnum
                - New enum values: [oauth2_client_credentials]

POST /api/user-invitations/check-duplicates/

- Description changed from 'Returns pending invitations that already exist for the same email and role within the given scope.' to 'Returns pending invitations that already exist for the same email and role within the given scope, along with the active roles those emails already hold in it.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: existing_roles
          - Properties changed
            - New property: existing_roles

GET /api/user-permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: source
              - Modified property: customer_name
                - Nullable changed from false to true
              - Modified property: customer_uuid
                - Nullable changed from false to true

GET /api/user-permissions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: source
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [details has_passkey passkey_count]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: details
              - New property: has_passkey
              - New property: passkey_count
              - Modified property: permissions
                - Items changed
                  - Properties changed
                    - New property: source
                    - Modified property: customer_name
                      - Nullable changed from false to true
                    - Modified property: customer_uuid
                      - Nullable changed from false to true

POST /api/users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: details
            - New property: has_passkey
            - New property: passkey_count
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: source
                  - Modified property: customer_name
                    - Nullable changed from false to true
                  - Modified property: customer_uuid
                    - Nullable changed from false to true

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [details has_passkey passkey_count]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: details
            - New property: has_passkey
            - New property: passkey_count
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - Modified property: customer_name
                    - Nullable changed from false to true
                  - Modified property: customer_uuid
                    - Nullable changed from false to true

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [details has_passkey passkey_count]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: details
            - New property: has_passkey
            - New property: passkey_count
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: source
                  - Modified property: customer_name
                    - Nullable changed from false to true
                  - Modified property: customer_uuid
                    - Nullable changed from false to true

PATCH /api/users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: details
            - New property: has_passkey
            - New property: passkey_count
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: source
                  - Modified property: customer_name
                    - Nullable changed from false to true
                  - Modified property: customer_uuid
                    - Nullable changed from false to true

PUT /api/users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: details
            - New property: has_passkey
            - New property: passkey_count
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: source
                  - Modified property: customer_name
                    - Nullable changed from false to true
                  - Modified property: customer_uuid
                    - Nullable changed from false to true

POST /api/users/{uuid}/refresh_token/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: token
          - Properties changed
            - Deleted property: token

GET /api/users/{uuid}/token/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: token
          - Properties changed
            - Deleted property: token

GET /api/version/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: changelog_summary

GET /api/vmware-datastores/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: capacity
                - Format changed from '' to 'int64'
                - Max changed from 2.147483647e+09 to 9.223372036854776e+18
              - Modified property: free_space
                - Format changed from '' to 'int64'
                - Max changed from 2.147483647e+09 to 9.223372036854776e+18

GET /api/vmware-datastores/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: capacity
              - Format changed from '' to 'int64'
              - Max changed from 2.147483647e+09 to 9.223372036854776e+18
            - Modified property: free_space
              - Format changed from '' to 'int64'
              - Max changed from 2.147483647e+09 to 9.223372036854776e+18
