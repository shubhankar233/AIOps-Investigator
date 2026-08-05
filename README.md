<!-- # AIOps Investigator

AI-Powered Incident Investigation Platform built with AWS Serverless and Amazon Bedrock.

## Project Goal

AIOps Investigator helps engineers investigate cloud incidents by:

- Uploading application logs
- Detecting important events
- Generating AI-powered incident analysis
- Retrieving similar historical incidents (Version 2)
- Providing structured root cause reports
- Tracking incident history

## Tech Stack

### Frontend
- React
- Vite
- TypeScript

### Backend
- Python 3.12
- AWS Lambda
- Amazon Bedrock

### AWS Services
- API Gateway
- Lambda
- DynamoDB
- CloudWatch
- IAM
- AWS SAM

## Development Status

- [x] Day 0 – Environment Setup
- [ ] Version 1 – Serverless MVP
- [ ] Version 2 – AI Engineering
- [ ] Version 3 – Production Engineering

## License

MITx     -->

# AIOps Investigator

> AI-powered cloud incident investigation platform built with AWS serverless services and Amazon Bedrock.

AIOps Investigator analyzes application and cloud logs, detects known failure patterns, retrieves similar historical incidents, and uses Amazon Bedrock to generate a probable root cause, reasoning, and remediation steps.

The goal is to reduce the time engineers spend manually reading logs during cloud incidents.

---

## Why AIOps Investigator?

When a production incident occurs, engineers often need to:

1. Read large amounts of logs.
2. Identify important error patterns.
3. Determine the likely root cause.
4. Search for similar incidents from the past.
5. Remember what fixed previous incidents.
6. Decide what remediation steps to take.

AIOps Investigator combines deterministic detection, historical incident retrieval, and AI-assisted investigation into a single workflow.

Instead of treating every incident as a completely new problem, the system uses previous investigations as contextual evidence.

---

## Core Workflow

```text
                    AIOps Investigator

User
 │
 │ Application / Cloud Logs
 ▼
React Frontend
 │
 │ HTTP POST
 ▼
Amazon API Gateway
 │
 ▼
AWS Lambda
 │
 ├── Rule Engine
 │      │
 │      └── Detect known failure patterns
 │
 ├── DynamoDB
 │      │
 │      └── Retrieve similar historical incidents
 │
 └── Amazon Bedrock
        │
        ├── Root-cause analysis
        ├── Reasoning
        └── Remediation recommendations
 │
 ▼
Investigation Result
 │
 ├── Severity
 ├── Detected Issues
 ├── Probable Root Cause
 ├── AI Reasoning
 ├── Remediation Steps
 └── Historical Context