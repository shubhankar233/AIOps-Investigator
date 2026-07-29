# API Design Document

# AIOps Investigator

**Version:** 1.0

**Status:** Draft

**API Style:** REST

**Data Format:** JSON

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.0 | July 2026 | Initial API Design | Shubhankar |

---

# Table of Contents

1. Overview
2. Design Principles
3. API Versioning
4. Authentication
5. Common Response Format
6. Error Response Format
7. Endpoints
8. HTTP Status Codes
9. Future APIs

---

# 1. Overview

The AIOps Investigator backend exposes REST APIs for uploading logs, retrieving investigations, and managing incident analysis.

All APIs communicate using JSON over HTTPS.

Current Version:

v1

Base URL:

/api/v1

---

# 2. Design Principles

The APIs follow these principles:

- RESTful
- Stateless
- JSON-based
- Predictable
- Versioned
- Consistent Error Handling
- Idempotent where applicable

---

# 3. API Versioning

Current Version

/api/v1

Future

/api/v2

Breaking changes will only occur in major API versions.

---

# 4. Authentication

Version 1

No authentication (development)

Future

JWT

Amazon Cognito

IAM Authorization

---

# 5. Common Response Format

Successful Response

{
    "success": true,
    "data": {},
    "message": "Operation successful"
}

---

Failed Response

{
    "success": false,
    "error": {
        "code": "INVALID_LOG",
        "message": "Uploaded log format is invalid"
    }
}

---

# 6. Error Response Format

| HTTP | Error |
|------|-------|
|400|Bad Request|
|401|Unauthorized|
|404|Not Found|
|422|Validation Failed|
|429|Rate Limited|
|500|Internal Server Error|

---

# 7. Endpoints

---

## POST /investigate

Description

Analyze uploaded logs.

Request

{
    "log_content":"..."
}

Success Response

{
    "incident_id":"INC-001",
    "summary":"...",
    "severity":"HIGH",
    "root_cause":"...",
    "recommendations":[]
}

Errors

400

422

500

---

## GET /incidents

Description

Return all investigations.

Response

[
   {
      "incident_id":"INC-001",
      "severity":"HIGH",
      "timestamp":"..."
   }
]

---

## GET /incidents/{incidentId}

Description

Retrieve one investigation.

Response

{
   "incident_id":"INC-001",
   "summary":"...",
   "analysis":{}
}

---

# 8. HTTP Status Codes

|Code|Meaning|
|----|-------|
|200|Success|
|201|Created|
|400|Bad Request|
|404|Not Found|
|422|Validation Error|
|500|Internal Error|

---

# 9. Future APIs

POST /evaluate

GET /metrics

POST /embeddings

POST /similar-incidents

GET /cost

GET /health