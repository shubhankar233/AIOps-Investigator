# Architecture Design Document (ADD)

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
| 1.0 | July 2026 | Initial Architecture Design Document | Shubhankar |

---

# Table of Contents

1. Introduction
2. Architecture Goals
3. Design Principles
4. High-Level Architecture
5. System Components
6. Request Lifecycle
7. Backend Architecture
8. Frontend Architecture
9. AI Processing Architecture
10. Data Architecture
11. API Architecture
12. Security Architecture
13. Configuration Management
14. Logging & Monitoring
15. Error Handling Strategy
16. Testing Architecture
17. Deployment Architecture
18. Version Evolution
19. Architecture Decision Records
20. Future Enhancements

---

# 1. Introduction

## Purpose

This document describes the software architecture of AIOps Investigator.

It serves as the primary technical blueprint for implementation by defining the system structure, component responsibilities, communication flow, and architectural decisions.

Unlike the Software Requirements Specification (SRS), which defines **what** the system must do, this document defines **how** the system is designed to achieve those requirements.

---

# 2. Architecture Goals

The architecture is designed to achieve the following goals:

- Modular
- Serverless
- Low Cost
- Maintainable
- Extensible
- Testable
- Cloud Native
- AI Ready
- Production Inspired

---

# 3. Design Principles

The project follows these engineering principles:

- Separation of Concerns
- Single Responsibility Principle
- Dependency Inversion
- Composition over Inheritance
- Infrastructure as Code
- Local First Development
- Fail Fast
- Cost Optimization
- Provider Abstraction
- Repository Pattern

---

# 4. High-Level Architecture

(Architecture diagram will be added here.)

---

# 5. System Components

## Presentation Layer

Responsibilities

- Upload logs
- Display reports
- View history
- Show evaluation metrics

Technology

- React
- Vite

---

## API Layer

Responsibilities

- Request routing
- Validation
- Error handling

Technology

- API Gateway

---

## Backend Layer

Responsibilities

- Process investigations
- Coordinate services
- Build AI prompts
- Store reports

Technology

- AWS Lambda
- Python

---

## AI Layer

Responsibilities

- AI provider abstraction
- Mock AI
- Bedrock integration

---

## Data Layer

Responsibilities

- Store investigations
- Retrieve history

Technology

- DynamoDB

---

# 6. Request Lifecycle

1. User uploads logs.
2. Frontend sends request.
3. API Gateway receives request.
4. Lambda starts execution.
5. Logs are parsed.
6. Prompt is created.
7. AI analyzes logs.
8. JSON is validated.
9. Investigation is stored.
10. Response returned.
11. Dashboard displays report.

---

# 7. Backend Architecture

## Core Engine

Incident Investigation Engine

Modules

- Parser
- Noise Filter
- Prompt Builder
- AI Provider
- JSON Validator
- Repository
- Response Builder

Each module performs one responsibility.

---

# 8. Frontend Architecture

Pages

- Dashboard
- Upload Logs
- Incident Report
- Investigation History

Components

- Navbar
- Upload Form
- Report Viewer
- History Table
- Loading Spinner

---

# 9. AI Processing Architecture

Provider Pattern

AI Provider Interface

↓

Mock Provider

↓

Amazon Bedrock Provider

Benefits

- Easy testing
- Offline development
- Replaceable providers
- Lower development cost

---

# 10. Data Architecture

Primary Entity

Incident

Fields

- IncidentID
- Timestamp
- Summary
- Root Cause
- Severity
- Recommendations
- Processing Time
- Cost
- Original Log
- AI Model

Future

- Embeddings
- Similar Incident IDs
- Evaluation Metrics

---

# 11. API Architecture

REST API

Endpoints

POST /investigate

GET /incidents

GET /incident/{id}

Future

POST /evaluate

GET /metrics

---

# 12. Security Architecture

- IAM Least Privilege
- Environment Variables
- Input Validation
- JSON Validation
- HTTPS
- No hardcoded secrets

---

# 13. Configuration Management

Environment Profiles

- Local
- Development
- Production

Configuration Files

- local.json
- dev.json
- prod.json

---

# 14. Logging & Monitoring

Logging

- Lambda Logs
- Application Logs

Monitoring

- CloudWatch

Future

- Metrics Dashboard

---

# 15. Error Handling Strategy

Possible Errors

- Invalid Logs
- AI Timeout
- Invalid JSON
- Storage Failure

Strategy

- Retry
- Validation
- Graceful Failure
- Error Messages

---

# 16. Testing Architecture

Unit Tests

Integration Tests

Mock AI Tests

Schema Validation

Performance Tests

Future

Evaluation Tests

---

# 17. Deployment Architecture

Infrastructure

AWS SAM

Deployment

One Command

Cleanup

One Command

Local Development

SAM Local

---

# 18. Version Evolution

## Version 1

Upload

↓

Parser

↓

AI

↓

Store

---

## Version 1.5

Evaluation Engine

---

## Version 2

Embeddings

FAISS

RAG

---

## Version 3

CloudWatch

CI/CD

Monitoring

EventBridge

---

# 19. Architecture Decision Records

Major architectural decisions are documented separately inside

docs/adr/

Examples

- Why AWS SAM
- Why DynamoDB
- Why Mock AI
- Why Provider Pattern
- Why Repository Pattern
- Why Local FAISS

---

# 20. Future Enhancements

- Multi-Agent AI
- ECS Support
- EKS Support
- CloudTrail Analysis
- Automated Remediation
- Authentication
- RBAC
- Production Scaling

---

## Architecture Diagram

> **Note:** This diagram will be generated after the implementation is complete to ensure it accurately reflects the final system architecture.