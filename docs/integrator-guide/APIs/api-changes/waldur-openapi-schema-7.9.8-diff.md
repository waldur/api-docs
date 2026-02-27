# OpenAPI schema diff - 7.9.8

## For version 7.9.8

### New Endpoints: 9

--------------------
GET /api/debug/pubsub/circuit_breaker/  
POST /api/debug/pubsub/circuit_breaker_reset/  
GET /api/debug/pubsub/dead_letter_queue/  
GET /api/debug/pubsub/message_state_cache/  
GET /api/debug/pubsub/metrics/  
POST /api/debug/pubsub/metrics_reset/  
GET /api/debug/pubsub/overview/  
GET /api/debug/pubsub/queues/  
POST /api/invoices/import_usage/  

### Deleted Endpoints: 7

------------------------
GET /api/checklists-admin-categories/  
HEAD /api/checklists-admin-categories/  
POST /api/checklists-admin-categories/  
DELETE /api/checklists-admin-categories/{uuid}/  
GET /api/checklists-admin-categories/{uuid}/  
PATCH /api/checklists-admin-categories/{uuid}/  
PUT /api/checklists-admin-categories/{uuid}/  

### Modified Endpoints: 16

--------------------------
POST /api/chat/stream/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/x-ndjson
        - Schema changed
          - Properties changed
            - New property: h
            - New property: n
            - New property: r
            - Modified property: k
              - Description changed from 'Component Alias (e.g. 'markdown', 'code').' to 'Component Alias (e.g. 'markdown', 'code', 'table').'

GET /api/checklists-admin/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: category_name
              - Deleted required property: category_uuid
            - Properties changed
              - Deleted property: category
              - Deleted property: category_name
              - Deleted property: category_uuid

POST /api/checklists-admin/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: category
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: category_name
            - Deleted required property: category_uuid
          - Properties changed
            - Deleted property: category
            - Deleted property: category_name
            - Deleted property: category_uuid

GET /api/checklists-admin/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: category_name
            - Deleted required property: category_uuid
          - Properties changed
            - Deleted property: category
            - Deleted property: category_name
            - Deleted property: category_uuid

PATCH /api/checklists-admin/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: category
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: category_name
            - Deleted required property: category_uuid
          - Properties changed
            - Deleted property: category
            - Deleted property: category_name
            - Deleted property: category_uuid

PUT /api/checklists-admin/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: category
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: category_name
            - Deleted required property: category_uuid
          - Properties changed
            - Deleted property: category
            - Deleted property: category_name
            - Deleted property: category_uuid

GET /api/invoice-items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: customer_name
              - New required property: customer_uuid
              - New required property: price
              - New required property: project_name
              - New required property: project_uuid
            - Properties changed
              - New property: customer_name
              - New property: customer_uuid
              - New property: price
              - New property: project_name
              - New property: project_uuid

GET /api/invoice-items/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: price
            - New required property: project_name
            - New required property: project_uuid
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid
            - New property: price
            - New property: project_name
            - New property: project_uuid

GET /api/invoice-items/{uuid}/consumptions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: price
            - New required property: project_name
            - New required property: project_uuid
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid
            - New property: price
            - New property: project_name
            - New property: project_uuid

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
                    - Modified property: project_uuid
                      - Nullable changed from false to true

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
                  - Modified property: project_uuid
                    - Nullable changed from false to true

GET /api/invoices/{uuid}/items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_uuid
              - Nullable changed from false to true

POST /api/invoices/{uuid}/paid/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: items
              - Items changed
                - Properties changed
                  - Modified property: project_uuid
                    - Nullable changed from false to true

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/checklists_summary/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: category_name
            - Properties changed
              - Deleted property: category_name

GET /api/provider-invoice-items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_uuid
                - Nullable changed from false to true

GET /api/provider-invoice-items/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_uuid
              - Nullable changed from false to true
