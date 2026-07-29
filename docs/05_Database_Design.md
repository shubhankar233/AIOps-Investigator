# Database Design

# AIOps Investigator

**Version:** 1.0

---

# Overview

Version 1 stores all investigations in a single DynamoDB table.

The schema is optimized for simple retrieval while remaining extensible for future AI capabilities.

---

# Table

IncidentTable

Primary Key

Partition Key

IncidentID

Example

INC-000001

---

# Attributes

|Attribute|Type|
|---------|----|
|IncidentID|String|
|Timestamp|String|
|Severity|String|
|Summary|String|
|RootCause|String|
|Recommendations|List|
|OriginalLog|String|
|Model|String|
|Latency|Number|
|Cost|Number|
|Status|String|

---

# Access Patterns

Retrieve Incident by ID

Retrieve Latest Incidents

Retrieve High Severity Incidents

Retrieve Investigations by Date

---

# Future Attributes

Embedding

EvaluationScore

HallucinationScore

SimilarIncidents

---

# Data Lifecycle

Create Investigation

↓

Store

↓

Retrieve

↓

Archive (Future)

↓

Delete (Future)

---

# Indexes

Version 1

Primary Key Only

Version 2

GSI

SeverityIndex

TimestampIndex