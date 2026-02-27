# OpenAPI schema diff - 7.9.7

## For version 7.9.7

### New Endpoints: 144

----------------------
GET /api/assignment-batches/  
HEAD /api/assignment-batches/  
POST /api/assignment-batches/  
DELETE /api/assignment-batches/{uuid}/  
GET /api/assignment-batches/{uuid}/  
PATCH /api/assignment-batches/{uuid}/  
PUT /api/assignment-batches/{uuid}/  
POST /api/assignment-batches/{uuid}/cancel/  
POST /api/assignment-batches/{uuid}/extend-deadline/  
POST /api/assignment-batches/{uuid}/send/  
GET /api/assignment-items/  
HEAD /api/assignment-items/  
POST /api/assignment-items/  
DELETE /api/assignment-items/{uuid}/  
GET /api/assignment-items/{uuid}/  
PATCH /api/assignment-items/{uuid}/  
PUT /api/assignment-items/{uuid}/  
POST /api/assignment-items/{uuid}/accept/  
POST /api/assignment-items/{uuid}/decline/  
POST /api/assignment-items/{uuid}/reassign/  
GET /api/assignment-items/{uuid}/suggest_alternatives/  
GET /api/call-assignment-configurations/  
HEAD /api/call-assignment-configurations/  
POST /api/call-assignment-configurations/  
DELETE /api/call-assignment-configurations/{uuid}/  
GET /api/call-assignment-configurations/{uuid}/  
PATCH /api/call-assignment-configurations/{uuid}/  
PUT /api/call-assignment-configurations/{uuid}/  
GET /api/call-reviewer-pools/  
HEAD /api/call-reviewer-pools/  
GET /api/call-reviewer-pools/{uuid}/  
PATCH /api/call-reviewer-pools/{uuid}/  
POST /api/call-reviewer-pools/{uuid}/accept/  
POST /api/call-reviewer-pools/{uuid}/decline/  
POST /api/chat-tools/execute/  
GET /api/coi-detection-jobs/  
HEAD /api/coi-detection-jobs/  
GET /api/coi-detection-jobs/{uuid}/  
GET /api/coi-disclosures/  
HEAD /api/coi-disclosures/  
POST /api/coi-disclosures/  
GET /api/coi-disclosures/{uuid}/  
GET /api/conflicts-of-interest/  
HEAD /api/conflicts-of-interest/  
GET /api/conflicts-of-interest/{uuid}/  
PATCH /api/conflicts-of-interest/{uuid}/  
PUT /api/conflicts-of-interest/{uuid}/  
POST /api/conflicts-of-interest/{uuid}/dismiss/  
POST /api/conflicts-of-interest/{uuid}/recuse/  
POST /api/conflicts-of-interest/{uuid}/waive/  
GET /api/expertise-categories/  
HEAD /api/expertise-categories/  
GET /api/expertise-categories/{uuid}/  
GET /api/marketplace-site-agent-connection-stats/  
POST /api/marketplace-site-agent-identities/cleanup_orphaned/  
DELETE /api/marketplace-site-agent-processors/{uuid}/  
POST /api/marketplace-site-agent-services/cleanup_stale/  
DELETE /api/marketplace-site-agent-services/{uuid}/  
GET /api/marketplace-site-agent-stats/  
GET /api/marketplace-site-agent-task-stats/  
GET /api/my-assignment-batches/  
HEAD /api/my-assignment-batches/  
GET /api/my-assignment-batches/{uuid}/  
GET /api/onboarding-verifications/available_checklists/  
HEAD /api/onboarding-verifications/available_checklists/  
GET /api/onboarding/person-identifier-fields/  
GET /api/proposal-protected-calls/{uuid}/affinity-matrix/  
GET /api/proposal-protected-calls/{uuid}/coi-configuration/  
PATCH /api/proposal-protected-calls/{uuid}/coi-configuration/  
POST /api/proposal-protected-calls/{uuid}/compute-affinities/  
GET /api/proposal-protected-calls/{uuid}/conflict-summary/  
GET /api/proposal-protected-calls/{uuid}/conflicts/  
POST /api/proposal-protected-calls/{uuid}/create-manual-assignment/  
POST /api/proposal-protected-calls/{uuid}/detect-conflicts/  
POST /api/proposal-protected-calls/{uuid}/generate-assignments/  
POST /api/proposal-protected-calls/{uuid}/generate-suggestions/  
POST /api/proposal-protected-calls/{uuid}/invite-by-email/  
GET /api/proposal-protected-calls/{uuid}/matching-configuration/  
PATCH /api/proposal-protected-calls/{uuid}/matching-configuration/  
GET /api/proposal-protected-calls/{uuid}/proposed-assignments/  
GET /api/proposal-protected-calls/{uuid}/reviewer-pool/  
POST /api/proposal-protected-calls/{uuid}/reviewer-pool/  
POST /api/proposal-protected-calls/{uuid}/send-all-assignments/  
POST /api/proposal-protected-calls/{uuid}/send-invitations/  
GET /api/proposal-protected-calls/{uuid}/suggestions/  
GET /api/rabbitmq-overview/  
GET /api/rabbitmq-stats/  
POST /api/rabbitmq-stats/  
GET /api/reviewer-bids/  
HEAD /api/reviewer-bids/  
POST /api/reviewer-bids/  
POST /api/reviewer-bids/bulk-submit/  
GET /api/reviewer-bids/my-bids/  
HEAD /api/reviewer-bids/my-bids/  
POST /api/reviewer-bids/submit/  
DELETE /api/reviewer-bids/{uuid}/  
GET /api/reviewer-bids/{uuid}/  
PATCH /api/reviewer-bids/{uuid}/  
PUT /api/reviewer-bids/{uuid}/  
GET /api/reviewer-invitations/{token}/  
POST /api/reviewer-invitations/{token}/accept/  
POST /api/reviewer-invitations/{token}/decline/  
GET /api/reviewer-profiles/  
HEAD /api/reviewer-profiles/  
POST /api/reviewer-profiles/  
GET /api/reviewer-profiles/me/  
HEAD /api/reviewer-profiles/me/  
PATCH /api/reviewer-profiles/me/  
POST /api/reviewer-profiles/me/  
POST /api/reviewer-profiles/publish/  
POST /api/reviewer-profiles/unpublish/  
GET /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/  
POST /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/  
DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/  
GET /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/  
PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/  
PUT /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/  
GET /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/  
POST /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/  
DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/  
GET /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/  
PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/  
PUT /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/  
GET /api/reviewer-profiles/{reviewer_profile_uuid}/publications/  
POST /api/reviewer-profiles/{reviewer_profile_uuid}/publications/  
DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/  
GET /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/  
PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/  
PUT /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/  
DELETE /api/reviewer-profiles/{uuid}/  
GET /api/reviewer-profiles/{uuid}/  
PATCH /api/reviewer-profiles/{uuid}/  
PUT /api/reviewer-profiles/{uuid}/  
GET /api/reviewer-profiles/{uuid}/connect-orcid/  
POST /api/reviewer-profiles/{uuid}/connect-orcid/callback/  
POST /api/reviewer-profiles/{uuid}/disconnect-orcid/  
POST /api/reviewer-profiles/{uuid}/import-publications/  
POST /api/reviewer-profiles/{uuid}/sync-orcid/  
GET /api/reviewer-suggestions/  
HEAD /api/reviewer-suggestions/  
DELETE /api/reviewer-suggestions/{uuid}/  
GET /api/reviewer-suggestions/{uuid}/  
POST /api/reviewer-suggestions/{uuid}/confirm/  
POST /api/reviewer-suggestions/{uuid}/reject/  

### Deleted Endpoints: 8

------------------------
GET /api/onboarding-country-configs/  
HEAD /api/onboarding-country-configs/  
POST /api/onboarding-country-configs/  
DELETE /api/onboarding-country-configs/{uuid}/  
GET /api/onboarding-country-configs/{uuid}/  
PATCH /api/onboarding-country-configs/{uuid}/  
PUT /api/onboarding-country-configs/{uuid}/  
POST /api/proposal-reviews/{uuid}/accept/  

### Modified Endpoints: 110

---------------------------
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
                      - New property: resource_expiration_threshold
                      - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

POST /api/chat/stream/

- Responses changed
  - Modified response: 200
    - Description changed from 'LLM chat streamed response.' to ''
    - Content changed
      - New media type: application/x-ndjson

GET /api/checklists-admin-questions/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [onboarding_customer onboarding_intent]
    - Deleted enum values: [customer_onboarding]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: checklist_type
            - Properties changed
              - New property: checklist_type

HEAD /api/checklists-admin-questions/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [onboarding_customer onboarding_intent]
    - Deleted enum values: [customer_onboarding]

POST /api/checklists-admin-questions/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: checklist_type
          - Properties changed
            - New property: checklist_type

GET /api/checklists-admin-questions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: checklist_type
          - Properties changed
            - New property: checklist_type

PATCH /api/checklists-admin-questions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: checklist_type
          - Properties changed
            - New property: checklist_type

PUT /api/checklists-admin-questions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: checklist_type
          - Properties changed
            - New property: checklist_type

GET /api/checklists-admin/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [onboarding_customer onboarding_intent]
    - Deleted enum values: [customer_onboarding]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [onboarding_customer onboarding_intent]
      - Deleted enum values: [customer_onboarding]
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
                    - New enum values: [onboarding_customer onboarding_intent]
                    - Deleted enum values: [customer_onboarding]

HEAD /api/checklists-admin/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [onboarding_customer onboarding_intent]
    - Deleted enum values: [customer_onboarding]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [onboarding_customer onboarding_intent]
      - Deleted enum values: [customer_onboarding]

POST /api/checklists-admin/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [onboarding_customer onboarding_intent]
                - Deleted enum values: [customer_onboarding]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [onboarding_customer onboarding_intent]
                  - Deleted enum values: [customer_onboarding]

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
                  - New enum values: [onboarding_customer onboarding_intent]
                  - Deleted enum values: [customer_onboarding]

PATCH /api/checklists-admin/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [onboarding_customer onboarding_intent]
                - Deleted enum values: [customer_onboarding]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [onboarding_customer onboarding_intent]
                  - Deleted enum values: [customer_onboarding]

PUT /api/checklists-admin/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [onboarding_customer onboarding_intent]
                - Deleted enum values: [customer_onboarding]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [onboarding_customer onboarding_intent]
                  - Deleted enum values: [customer_onboarding]

GET /api/checklists-admin/{uuid}/questions/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [onboarding_customer onboarding_intent]
    - Deleted enum values: [customer_onboarding]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [onboarding_customer onboarding_intent]
      - Deleted enum values: [customer_onboarding]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: checklist_type
            - Properties changed
              - New property: checklist_type

GET /api/database-stats/

- Summary changed from 'Get database table statistics' to 'Get comprehensive database statistics'
- Description changed from 'Retrieves statistics about the database, including the top 10 largest tables by total size. This information is useful for monitoring and maintenance. Requires support user permissions.' to 'Retrieves comprehensive statistics about the PostgreSQL database including:
- **Table statistics**: Top 10 largest tables by size
- **Connection statistics**: Active, idle, and waiting connections with utilization
- **Database size**: Total size, data size, and index size
- **Cache performance**: Buffer cache and index hit ratios (should be >99%)
- **Transaction statistics**: Commits, rollbacks, deadlocks
- **Lock statistics**: Current locks and waiting queries
- **Maintenance statistics**: Dead tuples, vacuum needs, oldest transaction age
- **Active queries**: Currently running queries with duration
- **Query performance**: Sequential vs index scan ratios
- **Replication status**: WAL size and replication lag (if applicable)

This information is useful for monitoring, debugging, and performance tuning.
Requires support user permissions.'

- OperationID changed from 'database_stats_list' to 'database_stats_retrieve'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'array' to 'object'
          - Items changed
            - Schema deleted
          - Required changed
            - New required property: active_queries
            - New required property: cache_performance
            - New required property: connections
            - New required property: database_size
            - New required property: locks
            - New required property: maintenance
            - New required property: query_performance
            - New required property: replication
            - New required property: table_stats
            - New required property: transactions
          - Properties changed
            - New property: active_queries
            - New property: cache_performance
            - New property: connections
            - New property: database_size
            - New property: locks
            - New property: maintenance
            - New property: query_performance
            - New property: replication
            - New property: table_stats
            - New property: transactions
    - Headers changed
      - Deleted header: x-result-count

GET /api/event-subscriptions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: observable_objects
                - Description changed from '' to 'List of objects to observe. Each item must have 'object_type' (one of: order, user_role, resource, offering_user, importable_resources, service_account, course_account, resource_periodic_limits) and optionally 'object_id' (integer). Example: [{"object_type": "resource"}, {"object_type": "order", "object_id": 123}]'

POST /api/event-subscriptions/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: observable_objects
            - Description changed from '' to 'List of objects to observe. Each item must have 'object_type' (one of: order, user_role, resource, offering_user, importable_resources, service_account, course_account, resource_periodic_limits) and optionally 'object_id' (integer). Example: [{"object_type": "resource"}, {"object_type": "order", "object_id": 123}]'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: observable_objects
              - Description changed from '' to 'List of objects to observe. Each item must have 'object_type' (one of: order, user_role, resource, offering_user, importable_resources, service_account, course_account, resource_periodic_limits) and optionally 'object_id' (integer). Example: [{"object_type": "resource"}, {"object_type": "order", "object_id": 123}]'

GET /api/event-subscriptions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: observable_objects
              - Description changed from '' to 'List of objects to observe. Each item must have 'object_type' (one of: order, user_role, resource, offering_user, importable_resources, service_account, course_account, resource_periodic_limits) and optionally 'object_id' (integer). Example: [{"object_type": "resource"}, {"object_type": "order", "object_id": 123}]'

GET /api/identity-providers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: allowed_redirects

POST /api/identity-providers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_redirects
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_redirects

GET /api/identity-providers/{provider}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_redirects

PATCH /api/identity-providers/{provider}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_redirects
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_redirects

PUT /api/identity-providers/{provider}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_redirects
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_redirects

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
                      - New property: consent_data

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
                    - New property: consent_data

GET /api/marketplace-offering-users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consent_data]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: consent_data

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: consent_data

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consent_data]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: consent_data

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: consent_data

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: consent_data

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

GET /api/marketplace-provider-offerings/

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
                      - New property: resource_expiration_threshold
                      - New property: unique_resource_per_attribute

POST /api/marketplace-provider-offerings/

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

GET /api/marketplace-provider-offerings/{uuid}/tos_stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: accepted_consents_over_time
          - Properties changed
            - New property: accepted_consents_over_time

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: resource_expiration_threshold
              - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                      - New property: resource_expiration_threshold
                      - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                      - New property: resource_expiration_threshold
                      - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

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
                    - New property: resource_expiration_threshold
                    - New property: unique_resource_per_attribute

GET /api/marketplace-site-agent-identities/

- New query param: orphaned
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering
                - Description changed from '' to 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.'

HEAD /api/marketplace-site-agent-identities/

- New query param: orphaned

POST /api/marketplace-site-agent-identities/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: offering
            - Description changed from '' to 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering
              - Description changed from '' to 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.'

GET /api/marketplace-site-agent-identities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering
              - Description changed from '' to 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.'

PUT /api/marketplace-site-agent-identities/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: offering
            - Description changed from '' to 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering
              - Description changed from '' to 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.'

POST /api/marketplace-site-agent-identities/{uuid}/register_event_subscription/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: observable_objects
              - Description changed from '' to 'List of objects to observe. Each item must have 'object_type' (one of: order, user_role, resource, offering_user, importable_resources, service_account, course_account, resource_periodic_limits) and optionally 'object_id' (integer). Example: [{"object_type": "resource"}, {"object_type": "order", "object_id": 123}]'
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: observable_objects
              - Description changed from '' to 'List of objects to observe. Each item must have 'object_type' (one of: order, user_role, resource, offering_user, importable_resources, service_account, course_account, resource_periodic_limits) and optionally 'object_id' (integer). Example: [{"object_type": "resource"}, {"object_type": "order", "object_id": 123}]'

GET /api/marketplace-site-agent-processors/

- New query param: last_run_before
- New query param: stale

HEAD /api/marketplace-site-agent-processors/

- New query param: last_run_before
- New query param: stale

GET /api/marketplace-site-agent-services/

- New query param: modified_after
- New query param: modified_before
- New query param: stale

HEAD /api/marketplace-site-agent-services/

- New query param: modified_after
- New query param: modified_before
- New query param: stale

GET /api/onboarding-verifications/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: country
            - Properties changed
              - Modified property: country
                - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') for context. Can be inferred from validation_method.'

POST /api/onboarding-verifications/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: country
        - Properties changed
          - Modified property: country
            - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') for context. Can be inferred from validation_method.'
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: country
          - Properties changed
            - Modified property: country
              - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') for context. Can be inferred from validation_method.'

POST /api/onboarding-verifications/start_verification/

- Description changed from 'Start company validation process by creating a verification record. If a checklist is configured for the country, use checklist endpoints to submit additional answers. Then call run_validation to perform automatic validation.' to 'Start company validation process by creating a verification record. User selects validation_method (e.g., 'ariregister', 'wirtschaftscompass'). Checklists are used for intent and customer data collection. Then call run_validation to perform automatic validation or create manual justification.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: country
        - Properties changed
          - New property: validation_method
          - Deleted property: is_manual_validation
          - Modified property: country
            - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') - optional, for display context'
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: country
          - Properties changed
            - Modified property: country
              - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') for context. Can be inferred from validation_method.'

GET /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: country
          - Properties changed
            - Modified property: country
              - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') for context. Can be inferred from validation_method.'

PATCH /api/onboarding-verifications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: country
            - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') for context. Can be inferred from validation_method.'
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: country
          - Properties changed
            - Modified property: country
              - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') for context. Can be inferred from validation_method.'

PUT /api/onboarding-verifications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: country
        - Properties changed
          - Modified property: country
            - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') for context. Can be inferred from validation_method.'
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: country
          - Properties changed
            - Modified property: country
              - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') for context. Can be inferred from validation_method.'

GET /api/onboarding-verifications/{uuid}/checklist/

- Description changed from 'Get checklist with questions and existing answers.' to 'Get checklist with questions and existing answers. Supports both customer and intent checklists via checklist_type parameter.'
- New query param: checklist_type
- Modified query param: include_all
  - Description changed from 'If true, returns all questions including hidden ones (for dynamic form visibility). Default: false.' to 'If true, returns all questions including hidden ones.'
  - Schema changed
    - Default changed from null to false
- Responses changed
  - Deleted response: 400
  - Deleted response: 404

GET /api/onboarding-verifications/{uuid}/completion_status/

- Description changed from 'Get checklist completion status.' to 'Get checklist completion status. Supports both customer and intent checklists via checklist_type parameter.'
- New query param: checklist_type
- Responses changed
  - Deleted response: 400
  - Deleted response: 404

POST /api/onboarding-verifications/{uuid}/run_validation/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: civil_number
          - Deleted property: person_identifier
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: country
          - Properties changed
            - Modified property: country
              - Description changed from 'ISO country code (e.g., 'EE' for Estonia)' to 'ISO country code (e.g., 'EE', 'AT') for context. Can be inferred from validation_method.'

POST /api/onboarding-verifications/{uuid}/submit_answers/

- Description changed from 'Submit checklist answers.' to 'Submit answers to checklist questions. Automatically detects which checklist (customer or intent) each question belongs to.'
- Responses changed
  - Deleted response: 400
  - Deleted response: 404
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: can_customer_be_created
            - New required property: created
            - New required property: customer
            - New required property: customer_creation_error_message
            - New required property: error_message
            - New required property: error_traceback
            - New required property: justifications
            - New required property: modified
            - New required property: onboarding_metadata
            - New required property: raw_response
            - New required property: status
            - New required property: user
            - New required property: user_full_name
            - New required property: user_submitted_customer_data
            - New required property: uuid
            - New required property: validated_at
            - New required property: validation_method
            - New required property: verified_company_data
            - New required property: verified_user_roles
            - Deleted required property: completion
            - Deleted required property: detail
          - Properties changed
            - New property: can_customer_be_created
            - New property: country
            - New property: created
            - New property: customer
            - New property: customer_creation_error_message
            - New property: error_message
            - New property: error_traceback
            - New property: expires_at
            - New property: justifications
            - New property: legal_name
            - New property: legal_person_identifier
            - New property: modified
            - New property: onboarding_metadata
            - New property: raw_response
            - New property: status
            - New property: user
            - New property: user_full_name
            - New property: user_submitted_customer_data
            - New property: uuid
            - New property: validated_at
            - New property: validation_method
            - New property: verified_company_data
            - New property: verified_user_roles
            - Deleted property: completion
            - Deleted property: detail

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
                            - Modified property: plugin_options
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/MergedPluginOptions
                                  - Properties changed
                                    - New property: resource_expiration_threshold
                                    - New property: unique_resource_per_attribute

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
                                  - New property: resource_expiration_threshold
                                  - New property: unique_resource_per_attribute

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
                            - New property: resource_expiration_threshold
                            - New property: unique_resource_per_attribute

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
                          - New property: resource_expiration_threshold
                          - New property: unique_resource_per_attribute

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
                          - New property: resource_expiration_threshold
                          - New property: unique_resource_per_attribute

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
                          - New property: resource_expiration_threshold
                          - New property: unique_resource_per_attribute

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
                          - New property: resource_expiration_threshold
                          - New property: unique_resource_per_attribute

POST /api/openportal-unmanaged-projects/{uuid}/move_project/

- Description changed from 'Moves a project and its associated resources to a different customer. This is a staff-only action. You can choose whether to preserve existing project permissions for users.' to 'Moves a project and its associated resources to a different customer. This is a staff-only action. You can choose whether to preserve existing project permissions for users. Terminated projects can also be moved.'
- Responses changed
  - Deleted response: 400

GET /api/openstack-floating-ips/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [router]

GET /api/openstack-floating-ips/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [router]

GET /api/openstack-routers/

- New query param: state

HEAD /api/openstack-routers/

- New query param: state

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Request body changed

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: AUTOMATED_MATCHING_ENABLED
            - New property: COI_COAUTHORSHIP_LOOKBACK_YEARS
            - New property: COI_COAUTHORSHIP_THRESHOLD_PAPERS
            - New property: COI_DETECTION_ENABLED
            - New property: COI_DISCLOSURE_REQUIRED
            - New property: COI_INSTITUTIONAL_LOOKBACK_YEARS
            - New property: CROSSREF_MAILTO
            - New property: ONBOARDING_VALIDATION_METHODS
            - New property: ORCID_API_URL
            - New property: ORCID_AUTH_URL
            - New property: ORCID_CLIENT_ID
            - New property: ORCID_CLIENT_SECRET
            - New property: ORCID_REDIRECT_URI
            - New property: ORCID_SANDBOX_MODE
            - New property: REVIEWER_PROFILES_ENABLED
            - New property: SEMANTIC_SCHOLAR_API_KEY
            - New property: USER_ACTIONS_DEFAULT_EXPIRATION_REMINDERS
            - New property: USER_ACTIONS_ENABLED
            - New property: USER_ACTIONS_EXECUTION_RETENTION_DAYS
            - New property: USER_ACTIONS_HIGH_URGENCY_NOTIFICATION
            - New property: USER_ACTIONS_NOTIFICATION_THRESHOLD
            - New property: USER_ACTIONS_PENDING_ORDER_HOURS
            - Deleted property: ONBOARDING_COUNTRY

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: AUTOMATED_MATCHING_ENABLED
          - New property: COI_COAUTHORSHIP_LOOKBACK_YEARS
          - New property: COI_COAUTHORSHIP_THRESHOLD_PAPERS
          - New property: COI_DETECTION_ENABLED
          - New property: COI_DISCLOSURE_REQUIRED
          - New property: COI_INSTITUTIONAL_LOOKBACK_YEARS
          - New property: CROSSREF_MAILTO
          - New property: ONBOARDING_VALIDATION_METHODS
          - New property: ORCID_API_URL
          - New property: ORCID_AUTH_URL
          - New property: ORCID_CLIENT_ID
          - New property: ORCID_CLIENT_SECRET
          - New property: ORCID_REDIRECT_URI
          - New property: ORCID_SANDBOX_MODE
          - New property: REVIEWER_PROFILES_ENABLED
          - New property: SEMANTIC_SCHOLAR_API_KEY
          - New property: USER_ACTIONS_DEFAULT_EXPIRATION_REMINDERS
          - New property: USER_ACTIONS_ENABLED
          - New property: USER_ACTIONS_EXECUTION_RETENTION_DAYS
          - New property: USER_ACTIONS_HIGH_URGENCY_NOTIFICATION
          - New property: USER_ACTIONS_NOTIFICATION_THRESHOLD
          - New property: USER_ACTIONS_PENDING_ORDER_HOURS
          - Deleted property: ONBOARDING_COUNTRY
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: AUTOMATED_MATCHING_ENABLED
          - New property: COI_COAUTHORSHIP_LOOKBACK_YEARS
          - New property: COI_COAUTHORSHIP_THRESHOLD_PAPERS
          - New property: COI_DETECTION_ENABLED
          - New property: COI_DISCLOSURE_REQUIRED
          - New property: COI_INSTITUTIONAL_LOOKBACK_YEARS
          - New property: CROSSREF_MAILTO
          - New property: ONBOARDING_VALIDATION_METHODS
          - New property: ORCID_API_URL
          - New property: ORCID_AUTH_URL
          - New property: ORCID_CLIENT_ID
          - New property: ORCID_CLIENT_SECRET
          - New property: ORCID_REDIRECT_URI
          - New property: ORCID_SANDBOX_MODE
          - New property: REVIEWER_PROFILES_ENABLED
          - New property: SEMANTIC_SCHOLAR_API_KEY
          - New property: USER_ACTIONS_DEFAULT_EXPIRATION_REMINDERS
          - New property: USER_ACTIONS_ENABLED
          - New property: USER_ACTIONS_EXECUTION_RETENTION_DAYS
          - New property: USER_ACTIONS_HIGH_URGENCY_NOTIFICATION
          - New property: USER_ACTIONS_NOTIFICATION_THRESHOLD
          - New property: USER_ACTIONS_PENDING_ORDER_HOURS
          - Deleted property: ONBOARDING_COUNTRY
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: AUTOMATED_MATCHING_ENABLED
          - New property: COI_COAUTHORSHIP_LOOKBACK_YEARS
          - New property: COI_COAUTHORSHIP_THRESHOLD_PAPERS
          - New property: COI_DETECTION_ENABLED
          - New property: COI_DISCLOSURE_REQUIRED
          - New property: COI_INSTITUTIONAL_LOOKBACK_YEARS
          - New property: CROSSREF_MAILTO
          - New property: ONBOARDING_VALIDATION_METHODS
          - New property: ORCID_API_URL
          - New property: ORCID_AUTH_URL
          - New property: ORCID_CLIENT_ID
          - New property: ORCID_CLIENT_SECRET
          - New property: ORCID_REDIRECT_URI
          - New property: ORCID_SANDBOX_MODE
          - New property: REVIEWER_PROFILES_ENABLED
          - New property: SEMANTIC_SCHOLAR_API_KEY
          - New property: USER_ACTIONS_DEFAULT_EXPIRATION_REMINDERS
          - New property: USER_ACTIONS_ENABLED
          - New property: USER_ACTIONS_EXECUTION_RETENTION_DAYS
          - New property: USER_ACTIONS_HIGH_URGENCY_NOTIFICATION
          - New property: USER_ACTIONS_NOTIFICATION_THRESHOLD
          - New property: USER_ACTIONS_PENDING_ORDER_HOURS
          - Deleted property: ONBOARDING_COUNTRY

POST /api/projects/{uuid}/move_project/

- Description changed from 'Moves a project and its associated resources to a different customer. This is a staff-only action. You can choose whether to preserve existing project permissions for users.' to 'Moves a project and its associated resources to a different customer. This is a staff-only action. You can choose whether to preserve existing project permissions for users. Terminated projects can also be moved.'
- Responses changed
  - Deleted response: 400

GET /api/proposal-proposals/

- New query param: created_by_uuid
- New query param: my_proposals
- New query param: round_uuid

HEAD /api/proposal-proposals/

- New query param: created_by_uuid
- New query param: my_proposals
- New query param: round_uuid

GET /api/proposal-protected-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: reviewer_identity_visible_to_submitters
                - Description changed from 'Whether proposal submitters can see reviewer identities' to 'Whether proposal applicants can see reviewer identities'
              - Modified property: reviews_visible_to_submitters
                - Description changed from 'Whether proposal submitters can see review comments and scores' to 'Whether proposal applicants can see review comments and scores'

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: reviewer_identity_visible_to_submitters
            - Description changed from 'Whether proposal submitters can see reviewer identities' to 'Whether proposal applicants can see reviewer identities'
          - Modified property: reviews_visible_to_submitters
            - Description changed from 'Whether proposal submitters can see review comments and scores' to 'Whether proposal applicants can see review comments and scores'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: reviewer_identity_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see reviewer identities' to 'Whether proposal applicants can see reviewer identities'
            - Modified property: reviews_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see review comments and scores' to 'Whether proposal applicants can see review comments and scores'

GET /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: reviewer_identity_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see reviewer identities' to 'Whether proposal applicants can see reviewer identities'
            - Modified property: reviews_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see review comments and scores' to 'Whether proposal applicants can see review comments and scores'

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: reviewer_identity_visible_to_submitters
            - Description changed from 'Whether proposal submitters can see reviewer identities' to 'Whether proposal applicants can see reviewer identities'
          - Modified property: reviews_visible_to_submitters
            - Description changed from 'Whether proposal submitters can see review comments and scores' to 'Whether proposal applicants can see review comments and scores'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: reviewer_identity_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see reviewer identities' to 'Whether proposal applicants can see reviewer identities'
            - Modified property: reviews_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see review comments and scores' to 'Whether proposal applicants can see review comments and scores'

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: reviewer_identity_visible_to_submitters
            - Description changed from 'Whether proposal submitters can see reviewer identities' to 'Whether proposal applicants can see reviewer identities'
          - Modified property: reviews_visible_to_submitters
            - Description changed from 'Whether proposal submitters can see review comments and scores' to 'Whether proposal applicants can see review comments and scores'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: reviewer_identity_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see reviewer identities' to 'Whether proposal applicants can see reviewer identities'
            - Modified property: reviews_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see review comments and scores' to 'Whether proposal applicants can see review comments and scores'

POST /api/proposal-protected-calls/{uuid}/activate/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: message
          - Properties changed
            - New property: message
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
            - Deleted property: uuid

POST /api/proposal-protected-calls/{uuid}/archive/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: message
          - Properties changed
            - New property: message
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
            - Deleted property: uuid

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: reviewer_identity_visible_to_submitters
            - Description changed from 'Whether proposal submitters can see reviewer identities' to 'Whether proposal applicants can see reviewer identities'
          - Modified property: reviews_visible_to_submitters
            - Description changed from 'Whether proposal submitters can see review comments and scores' to 'Whether proposal applicants can see review comments and scores'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: reviewer_identity_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see reviewer identities' to 'Whether proposal applicants can see reviewer identities'
            - Modified property: reviews_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see review comments and scores' to 'Whether proposal applicants can see review comments and scores'

GET /api/proposal-public-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: reviewer_identity_visible_to_submitters
                - Description changed from 'Whether proposal submitters can see reviewer identities. If False, reviewers appear as 'Reviewer 1', 'Reviewer 2', etc.' to 'Whether proposal applicants can see reviewer identities. If False, reviewers appear as 'Reviewer 1', 'Reviewer 2', etc.'
              - Modified property: reviews_visible_to_submitters
                - Description changed from 'Whether proposal submitters can see review comments and scores. If False, submitters only see final approval/rejection status.' to 'Whether proposal applicants can see review comments and scores. If False, applicants only see final approval/rejection status.'

GET /api/proposal-public-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: reviewer_identity_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see reviewer identities. If False, reviewers appear as 'Reviewer 1', 'Reviewer 2', etc.' to 'Whether proposal applicants can see reviewer identities. If False, reviewers appear as 'Reviewer 1', 'Reviewer 2', etc.'
            - Modified property: reviews_visible_to_submitters
              - Description changed from 'Whether proposal submitters can see review comments and scores. If False, submitters only see final approval/rejection status.' to 'Whether proposal applicants can see review comments and scores. If False, applicants only see final approval/rejection status.'

GET /api/proposal-reviews/

- New query param: round_uuid
- Modified query param: state
  - Schema changed
    - Items changed
      - Deleted enum values: [created]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ProposalReviewStateEnum
                    - Deleted enum values: [created]

HEAD /api/proposal-reviews/

- New query param: round_uuid
- Modified query param: state
  - Schema changed
    - Items changed
      - Deleted enum values: [created]

POST /api/proposal-reviews/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProposalReviewStateEnum
                  - Deleted enum values: [created]

GET /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProposalReviewStateEnum
                  - Deleted enum values: [created]

PATCH /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProposalReviewStateEnum
                  - Deleted enum values: [created]

PUT /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProposalReviewStateEnum
                  - Deleted enum values: [created]

GET /api/rabbitmq-user-stats/

- Summary changed from '' to 'Get RabbitMQ user connection statistics'
- Description changed from '' to 'Returns enriched connection data for all RabbitMQ users.

For each user (which corresponds to an EventSubscription), provides:

- Connection state (running, blocked, blocking)
- Traffic statistics (bytes sent/received)
- Connection timestamp
- Client properties (product, version, platform)
- Channel count and heartbeat timeout

Requires support user permissions.'

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: connections
                - Description changed from '' to 'List of active connections with detailed statistics'
                - Items changed
                  - Required changed
                    - New required property: channels
                    - New required property: client_properties
                    - New required property: connected_at
                    - New required property: recv_oct
                    - New required property: send_oct
                    - New required property: state
                    - New required property: timeout
                  - Properties changed
                    - New property: channels
                    - New property: client_properties
                    - New property: connected_at
                    - New property: recv_oct
                    - New property: send_oct
                    - New property: state
                    - New property: timeout
                    - Modified property: source_ip
                      - Property 'OneOf' changed
                        - Schemas deleted: subschema #1, subschema #2
                      - Type changed from '' to 'string'
                      - Description changed from 'An IPv4 or IPv6 address.' to 'Client IP address'
                    - Modified property: vhost
                      - Description changed from '' to 'Virtual host name'
              - Modified property: username
                - Description changed from '' to 'RabbitMQ username (corresponds to EventSubscription UUID)'

GET /api/user-actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: route_params
            - Properties changed
              - New property: offering_uuid
              - New property: order_type
              - New property: resource_name
              - New property: resource_uuid
              - Modified property: route_params
                - Type changed from 'string' to 'object'
                - Description changed from 'Parameters for route navigation' to ''
                - ReadOnly changed from false to true
                - AdditionalProperties changed
                  - Schema added

GET /api/user-actions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: route_params
          - Properties changed
            - New property: offering_uuid
            - New property: order_type
            - New property: resource_name
            - New property: resource_uuid
            - Modified property: route_params
              - Type changed from 'string' to 'object'
              - Description changed from 'Parameters for route navigation' to ''
              - ReadOnly changed from false to true
              - AdditionalProperties changed
                - Schema added
