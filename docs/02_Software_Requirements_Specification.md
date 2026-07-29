# Software Requirements Specification (SRS)

# AIOps Investigator

**Version:** 1.0

**Status:** Draft

**Project Type:** AI-Powered Incident Investigation Platform

**Author:** Shubhankar

**Last Updated:** July 2026

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.0 | July 2026 | Initial SRS | Shubhankar |

---

# Table of Contents

1. Introduction
2. Overall Description
3. System Features
4. Functional Requirements
5. Non-Functional Requirements
6. User Stories
7. Use Cases
8. External Interface Requirements
9. Data Requirements
10. Business Rules
11. Constraints
12. Assumptions & Dependencies
13. Acceptance Criteria
14. Traceability Matrix
15. Appendix

---

# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for AIOps Investigator.

The document serves as the primary reference for designing, implementing, testing, and validating the software system. It establishes a common understanding among developers, reviewers, and future contributors regarding the expected behavior of the application before implementation begins.

The SRS focuses on defining what the system must accomplish while remaining independent of implementation details wherever possible.

---

## 1.2 Project Overview

AIOps Investigator is an AI-powered incident investigation platform that assists engineers in analyzing cloud application failures.

Instead of manually reading logs, users submit application log files to the platform. The system analyzes the logs, identifies probable root causes, classifies incident severity, generates structured investigation reports, and stores historical investigations for future reference.

Future versions extend the system with Retrieval-Augmented Generation (RAG), evaluation metrics, and production-grade cloud engineering capabilities.

---

## 1.3 Objectives

The objectives of the system are:

- Reduce manual log investigation effort.
- Generate structured incident reports.
- Improve consistency of incident analysis.
- Support explainable AI-generated recommendations.
- Maintain searchable historical investigations.
- Enable measurable evaluation of AI performance.
- Operate within a constrained cloud budget.
- Demonstrate production-inspired engineering practices.

---

## 1.4 Intended Audience

This document is intended for:

- Software Engineers
- AI Engineers
- Cloud Engineers
- Forward Deployed Engineers
- Technical Interviewers
- Future Contributors

---

## 1.5 Scope

Version 1 supports investigation of:

- AWS Lambda logs
- Amazon API Gateway logs

Future versions may extend support to additional AWS services while preserving the overall system architecture.

---

## 1.6 Definitions

| Term | Definition |
|------|------------|
| Incident | Unexpected application behavior requiring investigation |
| Investigation | AI-generated analysis of an incident |
| Root Cause | Primary reason responsible for the incident |
| Mock AI | Local deterministic AI implementation |
| Foundation Model | Large Language Model used for analysis |
| RAG | Retrieval-Augmented Generation |
| Evaluation Dataset | Collection of labeled incidents used for benchmarking |

---

## 1.7 References

- AWS Well-Architected Framework
- AWS SAM Documentation
- Amazon Bedrock Documentation
- JSON Schema Specification
- Retrieval-Augmented Generation Research

---

# 2. Overall Description

## 2.1 Product Perspective

AIOps Investigator is a standalone AI-assisted investigation platform designed using a modular architecture.

The system consists of:

- User Interface
- Backend API
- AI Processing Layer
- Data Storage Layer

Each layer is independently replaceable without affecting the overall architecture.

---

## 2.2 Product Functions

The system shall:

- Accept application log uploads.
- Parse log files.
- Remove unnecessary log entries.
- Generate structured AI prompts.
- Analyze incidents using AI.
- Validate AI responses.
- Store investigation reports.
- Retrieve historical investigations.
- Display results through a dashboard.

---

## 2.3 User Classes

Primary User:

Cloud Engineer

Secondary Users:

Software Engineer

AI Engineer

Forward Deployed Engineer

System Administrator

---

## 2.4 Operating Environment

Development:

- Windows
- Linux
- macOS

Deployment:

- AWS Serverless

Browser Support:

- Chrome
- Edge
- Firefox

---

## 2.5 Design Principles

- Modular
- Serverless
- Cost Optimized
- Extensible
- Testable
- Maintainable

---

## 2.6 Assumptions

- User possesses AWS credentials.
- Internet connectivity is available.
- Logs follow supported formats.

---

# 3. System Features

The system provides the following major features:

- User Authentication (Future)
- Log Upload
- Incident Parsing
- Noise Filtering
- AI Investigation
- JSON Validation
- Incident Storage
- Incident History
- Search
- Evaluation Dashboard
- Cost Dashboard
- Monitoring

---

# 4. Functional Requirements

## FR-1 Log Upload

The system shall allow users to upload log files.

---

## FR-2 Log Validation

The system shall validate uploaded files before processing.

---

## FR-3 Log Parsing

The system shall extract structured events from uploaded logs.

---

## FR-4 Incident Detection

The system shall identify relevant error events.

---

## FR-5 AI Analysis

The system shall generate structured incident reports using the configured AI provider.

---

## FR-6 JSON Validation

The system shall validate AI responses against a predefined schema.

---

## FR-7 Incident Storage

The system shall store investigation reports.

---

## FR-8 Incident History

The system shall display previous investigations.

---

## FR-9 Similar Incident Retrieval (V2)

The system shall retrieve historically similar incidents.

---

## FR-10 Evaluation Framework (V1.5)

The system shall measure AI accuracy using labeled datasets.

---

## FR-11 Cost Tracking

The system shall record AI inference costs.

---

## FR-12 Performance Tracking

The system shall record processing latency.

---

# 5. Non-Functional Requirements

## Performance

- Analysis time < 10 seconds
- Dashboard load time < 2 seconds

## Reliability

- JSON validation success ≥99%
- API availability ≥99%

## Security

- Principle of least privilege
- Input validation
- Secure credential management

## Scalability

- Stateless backend
- Horizontal scaling

## Maintainability

- Modular architecture
- Clean code
- Infrastructure as Code

## Cost

- Total AWS budget ≤ ₹1000

## Usability

- Simple dashboard
- Clear error messages

## Portability

- Local development support
- AWS deployment support

---

# 6. User Stories

As a Cloud Engineer,
I want to upload logs,
So that I can investigate failures quickly.

As a Software Engineer,
I want structured root-cause analysis,
So that debugging becomes easier.

As an AI Engineer,
I want measurable AI evaluation,
So that model improvements can be quantified.

As a Hiring Manager,
I want to understand the project architecture,
So that I can evaluate engineering ability.

---

# 7. Use Cases

UC-1 Upload Logs

Actor:
User

Precondition:
Application available

Flow:

Upload logs

Validate logs

Analyze incident

Generate report

Store report

Display results

---

UC-2 View History

Retrieve investigations

Display list

Open report

---

UC-3 Evaluate AI

Load evaluation dataset

Run analysis

Generate metrics

Display dashboard

---

# 8. External Interface Requirements

User Interface

- Web dashboard

API

- REST API

Supported Formats

- JSON
- TXT
- LOG

External Services

- Amazon Bedrock
- AWS Lambda
- API Gateway
- DynamoDB

---

# 9. Data Requirements

Primary Entity

Incident

Attributes

- Incident ID
- Timestamp
- Severity
- Summary
- Root Cause
- Recommendations
- Model Used
- Processing Time
- Cost
- Original Log

---

# 10. Business Rules

- Every investigation receives a unique identifier.
- Invalid AI responses shall not be stored.
- Only validated reports may appear in history.
- Mock AI shall be the default during development.
- Cloud deployment shall remain within the defined budget.

---

# 11. Constraints

- AWS-only implementation
- Infrastructure as Code
- Serverless architecture
- Budget ≤ ₹1000
- Local-first development
- One-command deployment
- One-command cleanup

---

# 12. Assumptions & Dependencies

Assumptions

- AWS account available
- Bedrock access enabled
- Docker installed

Dependencies

- AWS CLI
- AWS SAM CLI
- Docker Desktop
- Python
- Node.js

---

# 13. Acceptance Criteria

The system shall be considered complete when:

- Log upload works.
- AI investigation completes successfully.
- JSON validation succeeds.
- Reports are stored.
- Reports are viewable.
- Deployment is automated.
- Cleanup is automated.
- Documentation is complete.
- Unit tests pass.
- GitHub repository is ready.

---

# 14. Traceability Matrix

| Requirement | Module | Test |
|------------|--------|------|
| FR-1 | Upload API | Upload Test |
| FR-2 | Validator | Validation Test |
| FR-3 | Parser | Parser Test |
| FR-4 | Engine | Engine Test |
| FR-5 | AI Provider | AI Test |
| FR-6 | Validator | Schema Test |
| FR-7 | Repository | Database Test |
| FR-8 | Dashboard | UI Test |

---

# 15. Appendix

## Version History

Version 1
- Serverless MVP

Version 1.5
- Evaluation Framework

Version 2
- Retrieval-Augmented Generation

Version 3
- Production Engineering

---

## Glossary

Refer to Section 1.6 for terminology definitions.