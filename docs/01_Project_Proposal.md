# AIOps Investigator
## AI-Powered Incident Investigation Platform for AWS Serverless Environments

> **Version:** 2.0 (Draft)  
> **Status:** In Design  
> **Author:** Shubhankar  
> **Project Type:** Portfolio / Learning / Production-Inspired  
> **Target Roles:** AWS AI Engineer, Software Development Engineer (SDE-1), Forward Deployed Engineer (FDE), Cloud Engineer

---

# Table of Contents

- [1. Executive Summary](#1-executive-summary)
- [2. Background](#2-background)
- [3. Problem Statement](#3-problem-statement)
- [4. Project Scope (Version 1)](#4-project-scope-version-1)

---

# 1. Executive Summary

Modern cloud-native applications continuously generate operational data in the form of application logs, infrastructure events, and monitoring alerts. During production incidents, engineers often spend significant time collecting evidence, filtering noisy logs, correlating failures across services, and identifying the most probable root cause before remediation can begin. As distributed systems become increasingly complex, this investigation process becomes more manual, repetitive, and dependent on individual experience.

**AIOps Investigator** is an AI-assisted incident investigation platform designed to accelerate the early stages of production incident analysis for AWS serverless applications. The platform ingests operational logs from AWS Lambda and Amazon API Gateway, filters irrelevant information, retrieves similar historical incidents, and generates structured, explainable root-cause analyses using Amazon Bedrock.

Unlike many AI-powered log analysis demonstrations, this project emphasizes **engineering discipline** alongside AI capabilities. It incorporates Infrastructure as Code (AWS SAM), provider-agnostic AI architecture, Retrieval-Augmented Generation (RAG), structured response validation, measurable evaluation metrics, and cost-aware serverless deployment.

The objective is to demonstrate software engineering, cloud engineering, and AI engineering principles through a production-inspired AWS serverless application that is reproducible, extensible, measurable, and cost-efficient.

---

# 2. Background

Cloud-native systems increasingly rely on serverless and distributed architectures to improve scalability, availability, and operational efficiency. AWS services such as Lambda and API Gateway allow developers to build highly scalable applications without managing servers.

While these architectures simplify infrastructure management, they also generate large volumes of operational data. During production incidents, engineers frequently switch between monitoring dashboards, log search tools, documentation, and historical incident reports before identifying the underlying cause of a failure.

Recent advances in Foundation Models (FMs) have enabled AI systems to assist with summarization, reasoning, and information retrieval. However, many AI-based demonstrations primarily generate textual explanations from logs without validating the quality of those responses, incorporating historical context, or measuring improvements objectively.

This project explores how AI can be integrated into a modern AWS serverless architecture while maintaining software engineering best practices, measurable evaluation, explainability, and cost efficiency. Rather than acting as a simple chatbot, the platform is designed as an engineering assistant that supports structured incident investigation workflows.

---

# 3. Problem Statement

Investigating production incidents remains one of the most time-consuming activities in cloud operations. Engineers must manually identify relevant log entries, distinguish meaningful events from background noise, correlate failures across services, recall similar historical incidents, and determine appropriate remediation strategies.

Existing monitoring platforms provide powerful log collection and search capabilities but still rely heavily on manual interpretation. Many AI-assisted solutions improve this process by generating summaries or potential root-cause explanations. However, these systems often lack structured outputs, measurable evaluation, explainability, historical incident retrieval, and mechanisms to continuously improve the quality of generated analyses.

For individual developers and small engineering teams, additional constraints such as infrastructure cost, deployment complexity, and operational overhead further limit the practical adoption of AI-assisted incident investigation systems.

This project addresses these challenges by designing an AI-assisted incident investigation platform specifically for AWS serverless environments. The initial scope focuses on AWS Lambda and Amazon API Gateway incidents, enabling measurable evaluation within a well-defined problem domain while maintaining a low-cost architecture suitable for learning and experimentation.

---

# 4. Project Scope (Version 1)

## Scope Overview

Version 1 focuses on building a production-inspired Minimum Viable Product (MVP) for AI-assisted investigation of AWS serverless incidents.

Rather than attempting to support every cloud service, Version 1 intentionally focuses on a limited number of AWS services and incident categories. This enables measurable evaluation, rapid iteration, and better engineering quality.

---

## In Scope

### Supported AWS Services

- AWS Lambda
- Amazon API Gateway

### Supported Incident Types

#### AWS Lambda

- Function timeout
- Out of memory
- Unhandled exception
- Runtime or import error
- Invalid configuration

#### Amazon API Gateway

- HTTP 5XX responses
- Authentication failures
- Authorization failures
- Integration timeout
- Invalid request payload
- Rate limiting (429)

### Functional Features

- Upload log files
- Log preprocessing
- Noise filtering
- AI-powered root cause analysis
- Structured JSON responses
- JSON schema validation
- Incident report storage
- Incident history
- Mock AI mode
- Amazon Bedrock integration
- AWS SAM deployment
- One-command cleanup

---

## Out of Scope

### AWS Services

- Amazon ECS
- Amazon EKS
- Amazon EC2
- Amazon RDS
- Amazon S3 event analysis
- CloudTrail analysis
- IAM policy analysis
- EventBridge
- Step Functions

### AI Features

- Multi-agent workflows
- Autonomous remediation
- Continuous log streaming
- Fine-tuned models
- Bedrock Knowledge Bases
- Managed vector databases

### Enterprise Features

- Authentication
- Role-Based Access Control (RBAC)
- Multi-tenancy
- High Availability
- Multi-region deployment

---

## Assumptions

- AWS account is available.
- Amazon Bedrock model access can be enabled if required.
- Development primarily uses Mock AI mode.
- Cloud deployment occurs only when validating functionality or recording demonstrations.
- Historical incident data is generated during project development.
- The project is intended for educational and portfolio purposes.

---

## Design Principles

### Cost Efficiency

Maintain a total AWS cost below **₹1000** by favoring local development and deploying cloud resources only when necessary.

### Simplicity First

Every feature must justify its complexity. Prefer simpler solutions whenever they satisfy the project requirements.

### Explainability

Every AI-generated analysis should be transparent, reproducible, and supported by structured evidence.

### Engineering over Demonstration

The project prioritizes maintainability, testing, evaluation, and clean architecture over simply integrating AI services.

### Extensibility

The architecture should support future integration of additional AWS services, AI providers, and retrieval mechanisms with minimal code changes.

---

## Version 1 Deliverables

- [ ] React Dashboard
- [ ] AWS Lambda Backend
- [ ] API Gateway
- [ ] DynamoDB
- [ ] Amazon Bedrock Integration
- [ ] Mock AI Mode
- [ ] Structured Incident Reports
- [ ] Incident History
- [ ] AWS SAM Infrastructure
- [ ] One-command Deployment
- [ ] One-command Cleanup

---

## Current Status

| Section | Status |
|---------|--------|
| Executive Summary | ✅ Complete |
| Background | ✅ Complete |
| Problem Statement | ✅ Complete |
| Project Scope | ✅ Complete |
| Existing Solutions | ⏳ Pending |
| Proposed Solution | ⏳ Pending |
| Goals | ⏳ Pending |
| Architecture Overview | ⏳ Pending |

---

> **Architecture Decision**
>
> Version 1 intentionally supports only **AWS Lambda** and **Amazon API Gateway** incidents. Additional AWS services will be introduced in later versions after establishing a measurable evaluation framework and a stable architecture.


---

# 5. Existing Solutions and Gap Analysis

Modern cloud platforms and observability tools provide powerful capabilities for collecting, searching, and analyzing operational data. These tools significantly improve incident response workflows but often require engineers to manually interpret information or are designed for enterprise environments with higher operational complexity.

The following comparison summarizes commonly used approaches and identifies the design gap that AIOps Investigator aims to address.

| Solution | Strengths | Limitations |
|----------|-----------|-------------|
| **Amazon CloudWatch Logs Insights** | Fast log search, filtering, aggregation, and query capabilities | Requires engineers to manually interpret search results and determine the root cause of incidents |
| **Amazon Q Developer** | AI-assisted explanations, code recommendations, and operational assistance | Primarily designed as a developer assistant rather than a measurable incident investigation platform with evaluation and historical learning |
| **OpenSearch / ELK Stack** | Powerful search, indexing, dashboards, and analytics | Requires significant infrastructure management and operational overhead; not suitable for a low-cost learning environment |
| **Splunk** | Enterprise-grade observability and incident investigation | Commercial licensing, infrastructure complexity, and operational cost make it unsuitable for this project's budget and learning objectives |
| **Typical AI Log Analysis Demonstrations** | Quickly summarize logs using Large Language Models | Often stop at text generation without structured outputs, evaluation, historical retrieval, or measurable performance metrics |

---

## Identified Gap

Current solutions excel at **collecting**, **searching**, and **visualizing** operational data. Recent AI-powered demonstrations further assist engineers by generating summaries and possible root-cause explanations.

However, relatively few learning projects combine modern AI capabilities with disciplined software engineering practices that make system behavior measurable, reproducible, and continuously improvable.

Most portfolio implementations focus on connecting an LLM to an API rather than answering engineering questions such as:

- How accurate are the generated analyses?
- Does Retrieval-Augmented Generation improve root-cause identification?
- How much does each AI analysis cost?
- How long does each investigation take?
- Can malformed AI responses be detected and recovered automatically?
- Can historical investigations improve future analyses?
- Can the entire infrastructure be reproduced using Infrastructure as Code?

These questions are essential when building AI-assisted engineering systems but are frequently omitted from demonstration projects.

---

## Project Positioning

AIOps Investigator is **not intended to replace** enterprise observability platforms such as Amazon CloudWatch, OpenSearch, or Splunk.

Instead, it acts as an **AI-assisted investigation layer** that sits on top of operational logs and focuses on accelerating the early stages of incident investigation.

The project emphasizes:

- Structured and validated AI outputs instead of free-form responses.
- Historical incident retrieval using Retrieval-Augmented Generation (RAG).
- Measurable evaluation through a labeled incident dataset.
- Cost-aware serverless deployment suitable for individual developers.
- Explainable AI workflows that engineers can review and trust.
- Infrastructure managed entirely through AWS SAM.

By combining cloud engineering, AI engineering, and software engineering best practices, the project aims to demonstrate how AI can be integrated into incident investigation workflows while maintaining reproducibility, maintainability, and measurable system quality.

---

## Why This Project?

The objective of AIOps Investigator is not to compete with commercial observability platforms or enterprise AIOps products.

Instead, the project serves as a production-inspired engineering exercise that demonstrates the integration of modern AI capabilities within a serverless AWS architecture while maintaining software engineering best practices.

The project was designed to answer a practical engineering question:

> **How can AI-assisted incident investigation be implemented in a cost-efficient, measurable, and extensible manner using AWS serverless services?**

By intentionally limiting the scope to AWS Lambda and Amazon API Gateway incidents, the project prioritizes measurable quality, clean architecture, and iterative development over broad service coverage.

Future versions will expand support to additional AWS services while preserving the same engineering principles established in Version 1.

---

# 6. Proposed Solution

AIOps Investigator proposes a modular, serverless, and AI-assisted platform for investigating production incidents in AWS serverless environments. Rather than replacing existing monitoring or observability tools, the platform complements them by automating the initial stages of incident investigation and providing structured, explainable analysis.

The system follows a layered architecture where each component has a single responsibility. This design improves maintainability, testability, and extensibility while allowing individual components to evolve independently.

Version 1 focuses on investigating incidents generated by AWS Lambda and Amazon API Gateway. Engineers upload log files through a web interface, after which the platform performs preprocessing, AI-assisted analysis, response validation, and report generation. Investigation results are stored for future reference and comparison.

Unlike traditional AI demonstrations that generate free-form text, AIOps Investigator produces structured incident reports that can be validated, measured, and continuously improved.

---

## Core Workflow

The platform follows the workflow below.

1. Upload operational logs.
2. Parse and preprocess the logs.
3. Remove noisy or irrelevant entries.
4. Build a structured AI prompt.
5. Submit the prompt to the configured AI provider.
6. Validate the generated JSON response.
7. Store the investigation report.
8. Present the results through the web dashboard.

Future versions extend this workflow by retrieving similar historical incidents before AI analysis, allowing Retrieval-Augmented Generation (RAG) to improve response quality.

---

## Key Design Characteristics

### Serverless Architecture

The platform uses AWS serverless services to minimize operational overhead, simplify deployment, and reduce infrastructure costs.

### Provider-Agnostic AI Layer

AI functionality is abstracted behind a common interface, allowing different AI providers to be integrated without changing business logic.

Version 1 includes:

- Mock AI Provider
- Amazon Bedrock Provider

Future versions may support additional providers without architectural changes.

### Structured AI Responses

AI-generated incident analyses are returned as structured JSON instead of unstructured text.

Each investigation includes information such as:

- Incident summary
- Root cause
- Confidence score
- Severity
- Suggested remediation
- Supporting evidence

Structured outputs improve reliability, simplify storage, and enable automated evaluation.

### Explainability

Every AI recommendation should be traceable to observable log evidence rather than functioning as an opaque black-box response.

### Evaluation-Driven Development

The project treats AI outputs as measurable engineering artifacts.

Future versions will evaluate response quality using labeled incident datasets, enabling continuous improvement through objective performance metrics rather than subjective observation.

### Cost-Conscious Design

The platform is designed to remain within a total AWS development budget of ₹1000.

To achieve this objective:

- Local development is prioritized.
- Mock AI mode is used during feature development.
- Cloud resources are deployed only when necessary.
- Infrastructure is destroyed after demonstrations to avoid unnecessary charges.

---
## Engineering Principles

The following principles guide all architectural and implementation decisions throughout the project lifecycle.

### Simplicity Over Complexity

Features should remain as simple as possible while satisfying project requirements. Additional complexity must provide measurable value.

### Measure Before Optimizing

Every optimization should be supported by measurable improvements in accuracy, latency, cost, or maintainability.

### Local-First Development

Features should be developed and tested locally whenever possible to reduce cloud costs and accelerate development.

### Infrastructure as Code

All cloud resources must be reproducible using AWS SAM. Manual infrastructure configuration should be avoided except where AWS requires one-time account setup.

### Separation of Concerns

Business logic, AI providers, data access, presentation, and infrastructure should remain independent to improve maintainability and future extensibility.

### Incremental Delivery

The project follows an iterative development model. Each version delivers a complete, deployable system that can be demonstrated independently while serving as the foundation for subsequent enhancements.

### Reproducibility

Every deployment, experiment, and evaluation should produce reproducible results through version-controlled infrastructure, configuration, and datasets.

---

# 7. Project Goals

The primary objective of AIOps Investigator is to design and implement a production-inspired AI-assisted incident investigation platform that demonstrates software engineering, cloud engineering, and AI engineering principles through a measurable and reproducible AWS serverless architecture.

To ensure the project remains focused and measurable, the goals are organized into business, technical, and learning objectives.

---

## 7.1 Business Goals

The platform should provide meaningful assistance during the early stages of incident investigation by reducing the time engineers spend manually analyzing operational logs.

The system aims to:

- Accelerate initial root-cause investigation.
- Reduce manual log inspection.
- Produce consistent and structured incident reports.
- Preserve historical investigations for future reference.
- Improve investigation quality through AI-assisted reasoning.
- Demonstrate explainable AI rather than opaque text generation.

---

## 7.2 Technical Goals

The project should demonstrate modern cloud-native engineering practices while remaining maintainable, scalable, and cost-efficient.

Technical objectives include:

- Build a fully serverless AWS application.
- Deploy all infrastructure using AWS SAM.
- Implement a modular backend architecture.
- Support interchangeable AI providers through abstraction.
- Validate all AI-generated responses against a predefined JSON schema.
- Store structured investigation reports in DynamoDB.
- Design the architecture for future RAG integration.
- Maintain a clean separation between infrastructure, business logic, AI services, and presentation layers.

---

## 7.3 AI Engineering Goals

The project aims to demonstrate practical AI engineering techniques rather than simple LLM integration.

Objectives include:

- Generate structured root-cause analyses using Amazon Bedrock.
- Support provider-independent AI integration.
- Build prompts that produce deterministic JSON outputs.
- Implement response validation and error recovery.
- Retrieve historical incidents using Retrieval-Augmented Generation (Version 2).
- Evaluate AI performance using labeled datasets.
- Measure the impact of RAG on investigation quality.

---

## 7.4 Cloud Engineering Goals

The platform should showcase modern AWS development practices.

Objectives include:

- Design a cost-efficient serverless architecture.
- Minimize operational overhead.
- Automate deployment and cleanup.
- Use Infrastructure as Code for reproducibility.
- Monitor application behavior using CloudWatch.
- Keep total AWS development costs below ₹1000.

---

## 7.5 Software Engineering Goals

The project should reflect production-quality software engineering practices.

Objectives include:

- Write modular and maintainable code.
- Follow a layered architecture.
- Apply separation of concerns.
- Implement centralized configuration management.
- Provide automated testing.
- Produce comprehensive documentation.
- Maintain a clean Git history.
- Follow consistent coding standards.

---

## 7.6 Learning Goals

This project serves as a practical learning platform for modern cloud and AI engineering.

Upon completion, the project should demonstrate proficiency in:

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon Bedrock
- AWS SAM
- Infrastructure as Code
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- AI Evaluation
- REST API development
- React frontend development
- CI/CD fundamentals
- Production-style software architecture

---

## 7.7 Success Criteria

Version 1 will be considered successful when the following outcomes are achieved:

- A user can upload AWS Lambda or API Gateway logs.
- The system generates a structured incident report.
- Reports are successfully stored and retrieved.
- The entire infrastructure is deployable using a single command.
- The application can be destroyed using a single cleanup command.
- Mock AI mode and Amazon Bedrock mode both function correctly.
- The application remains within the defined AWS budget.

---

# 9. Success Metrics

The success of AIOps Investigator is measured using objective engineering metrics rather than subjective observations. Each metric evaluates a different aspect of the system, including software quality, AI performance, operational efficiency, and cloud cost.

These metrics provide a baseline for continuous improvement as the project evolves from Version 1 to Version 3.

---

## 9.1 Engineering Metrics

| Metric | Target |
|---------|---------|
| Infrastructure Deployment Success | 100% successful deployment using AWS SAM |
| Infrastructure Cleanup Success | 100% resource deletion without manual intervention |
| Local Development Support | Full functionality in Mock AI mode |
| API Availability | 99% success during testing |
| JSON Validation Success | ≥99% valid responses |
| Failed Request Recovery | Automatic retry for malformed AI responses |

---

## 9.2 AI Performance Metrics

The quality of AI-generated incident investigations will be measured using a manually labeled evaluation dataset.

| Metric | Target |
|---------|---------|
| Root Cause Accuracy | ≥80% |
| Severity Classification Accuracy | ≥90% |
| JSON Schema Compliance | 100% |
| Evidence Citation Accuracy | ≥90% |
| Hallucination Rate | <5% |

These metrics will be evaluated using a representative dataset of serverless incident scenarios.

---

## 9.3 Retrieval-Augmented Generation (RAG) Metrics

Version 2 introduces historical incident retrieval. The effectiveness of RAG will be measured by comparing AI performance before and after retrieval.

| Metric | Target |
|---------|---------|
| Root Cause Accuracy Improvement | ≥10 percentage points |
| Similar Incident Retrieval Precision | ≥80% |
| Average Retrieval Latency | <500 ms |

A baseline evaluation will be recorded before RAG implementation to quantify the impact of historical context.

---

## 9.4 Performance Metrics

The application should remain responsive while maintaining low operational costs.

| Metric | Target |
|---------|---------|
| Average Analysis Time | <10 seconds |
| Dashboard Load Time | <2 seconds |
| Lambda Cold Start Impact | Minimized |
| Average API Response Time | <2 seconds |

Performance measurements will be recorded during testing and documented in the project repository.

---

## 9.5 Cost Metrics

The project is intentionally designed as a low-cost engineering portfolio.

| Metric | Target |
|---------|---------|
| Total AWS Development Cost | ≤ ₹1000 |
| Average AI Analysis Cost | Recorded for every deployment |
| Mock AI Usage During Development | >90% of development time |
| Idle Cloud Resources | None |

All infrastructure will be deployed only when required and destroyed after validation to prevent unnecessary charges.

---

## 9.6 Software Quality Metrics

Software quality will be evaluated using engineering best practices.

| Metric | Target |
|---------|---------|
| Unit Test Coverage | ≥70% |
| Linting Errors | Zero |
| Critical Security Issues | Zero |
| Configuration Through Environment Variables | 100% |
| Infrastructure Managed as Code | 100% |

---

## 9.7 Documentation Metrics

Project documentation should enable another developer to understand, deploy, and extend the system without additional guidance.

| Metric | Target |
|---------|---------|
| Architecture Documentation | Complete |
| Deployment Guide | Complete |
| API Documentation | Complete |
| Database Documentation | Complete |
| Evaluation Methodology | Complete |
| README Completeness | Complete |

---

## 9.8 Resume Readiness Checklist

The project will be considered portfolio-ready when all of the following criteria have been satisfied.

- [ ] End-to-end serverless application deployed successfully.
- [ ] AI-generated incident reports validated through JSON schema.
- [ ] Historical incident retrieval implemented.
- [ ] Evaluation dataset created and documented.
- [ ] AI performance measured and reported.
- [ ] Cost analysis completed.
- [ ] Deployment automated using AWS SAM.
- [ ] Documentation finalized.
- [ ] GitHub repository published.
- [ ] Demonstration video recorded.

Completion of this checklist indicates that the project is ready for technical interviews, portfolio presentation, and public demonstration.

---

# 10. High-Level System Architecture

## Overview

AIOps Investigator follows a modular serverless architecture built entirely on AWS managed services. The system is designed around loosely coupled components, enabling independent development, testing, and future expansion while minimizing operational overhead.

The architecture separates the application into four logical layers:

- Presentation Layer
- Application Layer
- AI Processing Layer
- Data Layer

This separation improves maintainability, simplifies testing, and allows future enhancements without significant architectural changes.

---

## Architecture Overview

```text
                +----------------------+
                |    React Frontend    |
                +----------+-----------+
                           |
                           |
                    HTTPS REST API
                           |
                           v
                 +----------------------+
                 |    API Gateway       |
                 +----------+-----------+
                           |
                           |
                           v
                 +----------------------+
                 | AWS Lambda Backend   |
                 +----------+-----------+
                           |
          +----------------+----------------+
          |                                 |
          |                                 |
          v                                 v
+----------------------+        +----------------------+
| AI Provider Layer    |        | Incident Repository  |
|                      |        |                      |
| Mock AI              |        | Amazon DynamoDB      |
| Amazon Bedrock       |        |                      |
+----------+-----------+        +----------+-----------+
           |                               ^
           |                               |
           +-------------------------------+
                   Store Investigation
```

---

## Architecture Layers

### 1. Presentation Layer

The Presentation Layer provides the user interface through which engineers interact with the platform.

Responsibilities include:

- Uploading log files
- Viewing incident reports
- Browsing investigation history
- Displaying AI-generated analysis
- Showing evaluation metrics

Technology:

- React
- TypeScript (future enhancement)
- REST API communication

---

### 2. Application Layer

The Application Layer contains the core business logic responsible for processing user requests.

Responsibilities include:

- Log parsing
- Input validation
- Request orchestration
- Prompt construction
- JSON validation
- Error handling
- Configuration management

Technology:

- AWS Lambda
- Python

---

### 3. AI Processing Layer

The AI Processing Layer abstracts all interaction with Foundation Models.

Instead of coupling the application directly to Amazon Bedrock, all AI communication passes through a provider interface.

This enables:

- Mock AI during development
- Amazon Bedrock in production
- Future provider expansion
- Easier testing

Initial Providers:

- Mock AI Provider
- Amazon Bedrock Provider

Future Providers:

- OpenAI
- Anthropic
- Azure OpenAI

---

### 4. Data Layer

The Data Layer stores all generated investigation reports.

Responsibilities include:

- Incident storage
- Investigation history
- AI response persistence
- Metadata storage

Technology:

- Amazon DynamoDB

Future versions may introduce vector storage for Retrieval-Augmented Generation while preserving the existing repository abstraction.

---

## Architectural Characteristics

The architecture follows several engineering principles.

| Characteristic | Description |
|---------------|-------------|
| Serverless | No infrastructure management |
| Event Driven | Request-based processing |
| Modular | Independent components |
| Extensible | New AI providers can be added easily |
| Cost Optimized | Local-first development with on-demand cloud usage |
| Testable | Mock AI enables offline development |
| Reproducible | Entire infrastructure defined using AWS SAM |

---

## Request Lifecycle

A typical investigation follows the sequence below.

1. User uploads a log file.
2. Frontend sends the request to API Gateway.
3. API Gateway invokes the backend Lambda function.
4. Lambda validates the uploaded data.
5. Relevant log entries are extracted.
6. A structured AI prompt is generated.
7. The configured AI provider analyzes the incident.
8. The response is validated against the predefined JSON schema.
9. The investigation report is stored in DynamoDB.
10. The structured report is returned to the frontend.
11. The dashboard displays the completed investigation.

---

## Version Evolution

The architecture is intentionally designed to evolve incrementally.

| Version | Primary Capability |
|----------|--------------------|
| Version 1 | AI-assisted incident investigation |
| Version 2 | Historical retrieval using RAG and evaluation framework |
| Version 3 | Event-driven processing, CI/CD, monitoring, and production engineering |

Each version builds upon the previous architecture without requiring major redesigns.

---

Frontend
    │
    ▼
API Gateway
    │
    ▼
Lambda
    │
    ▼
Incident Investigation Engine
    ├── Log Parser
    ├── Noise Filter
    ├── Prompt Builder
    ├── AI Provider
    ├── JSON Validator
    ├── Incident Repository
    └── Evaluation Module (V2)

---

# 11. Technology Stack

## Overview

The technology stack has been selected to satisfy the project's engineering goals of low operational cost, reproducibility, modularity, and extensibility. Preference has been given to managed AWS services and widely adopted open-source technologies that align with modern cloud-native development practices.

---

# Frontend

| Technology | Purpose | Reason for Selection |
|------------|---------|----------------------|
| React | User Interface | Component-based architecture, large ecosystem, industry standard |
| Vite | Frontend Build Tool | Fast development server and optimized production builds |
| TypeScript *(Future)* | Type Safety | Improves maintainability and reduces runtime errors |

---

# Backend

| Technology | Purpose | Reason for Selection |
|------------|---------|----------------------|
| Python 3.12 | Backend Runtime | Excellent AWS support, strong AI ecosystem, readable syntax |
| AWS Lambda | Compute | Serverless execution with automatic scaling and pay-per-use pricing |
| API Gateway | REST API | Secure API exposure and seamless Lambda integration |

---

# Artificial Intelligence

| Technology | Purpose | Reason for Selection |
|------------|---------|----------------------|
| Amazon Bedrock | Foundation Model Access | Managed access to foundation models without infrastructure management |
| Mock AI Provider | Local Development | Enables rapid development without incurring cloud costs |
| Prompt Engineering | AI Interaction | Produces structured, explainable incident analyses |
| JSON Schema Validation | Response Validation | Ensures AI responses conform to the expected format |

---

# Data Storage

| Technology | Purpose | Reason for Selection |
|------------|---------|----------------------|
| Amazon DynamoDB | Incident Repository | Fully managed NoSQL database with serverless scaling |
| Local JSON Files *(Development)* | Offline Testing | Simplifies local development before cloud deployment |

---

# Infrastructure

| Technology | Purpose | Reason for Selection |
|------------|---------|----------------------|
| AWS SAM | Infrastructure as Code | Native serverless deployment framework with local testing support |
| AWS CLI | Resource Management | Standard AWS command-line interface |
| Docker | Local Lambda Execution | Required by AWS SAM for local Lambda emulation |

---

# Development Tools

| Technology | Purpose | Reason for Selection |
|------------|---------|----------------------|
| Git | Version Control | Distributed version control |
| GitHub | Source Code Management | Repository hosting, collaboration, and portfolio presentation |
| VS Code | Development Environment | Lightweight IDE with extensive extension ecosystem |
| PowerShell | Automation Scripts | Windows-native scripting for deployment and cleanup |

---

# Testing

| Technology | Purpose | Reason for Selection |
|------------|---------|----------------------|
| pytest | Unit Testing | Mature Python testing framework |
| SAM Local | Integration Testing | Local execution of serverless APIs |
| Mock AI Provider | AI Testing | Deterministic AI responses during development |

---

# Future Technologies

The following technologies are intentionally excluded from Version 1 but may be introduced in later versions.

| Technology | Planned Version | Purpose |
|------------|----------------|----------|
| FAISS | Version 2 | Local vector similarity search |
| Titan Embeddings | Version 2 | Semantic incident retrieval |
| GitHub Actions | Version 3 | Continuous Integration and Deployment |
| CloudWatch Logs | Version 3 | Live log ingestion |
| EventBridge | Version 3 | Event-driven workflows |
| Step Functions | Version 3 | Workflow orchestration |

---

## Technology Selection Principles

The technology stack was chosen according to the following principles:

- Prefer managed AWS services over self-managed infrastructure.
- Minimize operational complexity.
- Prioritize local-first development.
- Keep the project within the ₹1000 AWS budget.
- Select technologies commonly used in modern cloud engineering roles.
- Ensure every technology contributes meaningful portfolio value.

---

# 12. Project Roadmap

The project follows an incremental development approach. Each version delivers a complete, usable system while establishing the foundation for the next stage.

---

## Version 1 — Serverless MVP

### Objective

Build a complete AI-assisted incident investigation platform capable of analyzing AWS Lambda and API Gateway logs.

### Deliverables

- React dashboard
- REST API
- AWS Lambda backend
- API Gateway
- Amazon DynamoDB
- Mock AI provider
- Amazon Bedrock integration
- Structured JSON incident reports
- Deployment using AWS SAM
- One-command deployment
- One-command cleanup

---

## Version 1.5 — Engineering Validation

### Objective

Measure system quality before introducing Retrieval-Augmented Generation.

### Deliverables

- Incident taxonomy
- Labeled evaluation dataset
- AI evaluation framework
- JSON validation metrics
- Hallucination tracking
- Latency measurement
- Cost measurement
- Accuracy dashboard

---

## Version 2 — AI Engineering

### Objective

Improve investigation quality using Retrieval-Augmented Generation.

### Deliverables

- Titan Embeddings
- Local FAISS vector store
- Historical incident retrieval
- Similarity search
- Prompt enrichment
- Baseline vs RAG comparison
- Retrieval performance metrics

---

## Version 3 — Production Engineering

### Objective

Transform the application into a production-inspired cloud platform.

### Deliverables

- GitHub Actions CI/CD
- CloudWatch integration
- EventBridge
- Monitoring dashboard
- Production documentation
- Performance optimization
- Operational metrics

---

## Long-Term Vision

Future versions may expand support to additional AWS services including ECS, EKS, EC2, RDS, and CloudTrail while preserving the modular architecture established in Version 1.

---

# 13. Risk Analysis

Potential project risks have been identified together with mitigation strategies.

| Risk | Impact | Mitigation |
|------|--------|------------|
| AWS costs exceed budget | High | Use Mock AI during development and delete infrastructure after testing |
| Bedrock model unavailable | Medium | Continue development using Mock AI Provider |
| AI generates invalid JSON | High | Validate against JSON Schema and retry when required |
| Limited evaluation dataset | Medium | Build a manually labeled dataset during Version 1.5 |
| Feature scope grows too quickly | High | Freeze Version 1 scope and defer enhancements |
| AWS service quotas | Low | Use low-volume workloads during development |
| Local environment inconsistencies | Medium | Use Python virtual environments and Infrastructure as Code |
| Architecture becomes tightly coupled | Medium | Maintain provider abstraction and modular services |

---

## Risk Management Strategy

The project follows an iterative development model in which each version delivers a deployable milestone. New features are introduced only after the previous version is stable, tested, and documented.

This approach reduces technical debt, limits unnecessary complexity, and ensures that the project remains maintainable throughout development.

---

# 14. Expected Outcomes

Upon completion, AIOps Investigator will demonstrate the integration of cloud engineering, software engineering, and AI engineering principles within a single production-inspired AWS serverless application.

The completed project will include:

- AI-assisted incident investigation platform
- Production-inspired serverless architecture
- Infrastructure fully managed using AWS SAM
- Structured AI-generated incident reports
- Historical incident retrieval using RAG
- Evaluation framework with measurable accuracy
- Cost-aware cloud deployment
- Comprehensive engineering documentation
- Automated deployment and cleanup
- Public GitHub repository
- Technical demonstration video

The project is intended to serve as a portfolio artifact demonstrating engineering practices expected in modern cloud-native software development.

---

# 15. Future Enhancements

Potential future improvements include:

- Support for Amazon ECS
- Support for Amazon EKS
- Support for Amazon EC2
- Support for Amazon RDS
- CloudTrail analysis
- Multi-agent AI workflows
- Streaming log ingestion
- Notification integrations
- Authentication and authorization
- Role-Based Access Control (RBAC)
- Multi-tenant architecture
- Kubernetes deployment
- Automated remediation
- Fine-tuned domain-specific models

These enhancements are intentionally excluded from the current roadmap to preserve project focus and maintain a manageable development scope.

---

# 16. References

The design and implementation of this project are informed by the following resources:

- AWS Well-Architected Framework
- AWS Serverless Application Model (AWS SAM) Documentation
- Amazon Bedrock Documentation
- AWS Lambda Developer Guide
- Amazon API Gateway Developer Guide
- Amazon DynamoDB Documentation
- FAISS Documentation
- Retrieval-Augmented Generation (Lewis et al., 2020)
- JSON Schema Specification
- React Documentation

---