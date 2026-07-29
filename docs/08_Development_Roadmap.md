# Development Roadmap

# AIOps Investigator

**Version:** 1.0

**Status:** In Progress

**Duration:** 6–8 Weeks

**Daily Commitment:** 2–3 Hours

---

# Objective

This roadmap defines the implementation plan for AIOps Investigator.

The project is divided into incremental milestones where each phase delivers a working, demonstrable system.

Each milestone builds upon the previous one while remaining independently valuable.

---

# Overall Timeline

| Phase | Goal | Status |
|--------|------|--------|
| Phase 0 | Project Setup | ✅ Completed |
| Phase 1 | Serverless MVP | ⬜ Pending |
| Phase 1.5 | AI Evaluation Framework | ⬜ Pending |
| Phase 2 | Retrieval-Augmented Generation (RAG) | ⬜ Pending |
| Phase 3 | Production Engineering | ⬜ Pending |
| Final | Documentation & Portfolio | ⬜ Pending |

---

# Phase 0 — Environment & Project Setup

## Goal

Prepare a professional development environment.

### Tasks

- [x] Install Git
- [x] Install Python 3.12
- [x] Create Python Virtual Environment
- [x] Install Node.js
- [x] Install Docker Desktop
- [x] Install AWS CLI v2
- [x] Install AWS SAM CLI
- [x] Configure Git
- [ ] Configure AWS CLI
- [ ] Enable Amazon Bedrock Model Access
- [x] Initialize Git Repository
- [x] Create Initial Project Structure
- [x] Create Documentation

### Deliverables

- Local development environment
- Git repository
- Initial documentation
- Project structure

---

# Phase 1 — Serverless MVP

## Goal

Build a complete serverless AI-powered incident investigation platform.

---

## Sprint 1 — AWS Infrastructure

### Tasks

- [ ] Configure AWS CLI
- [ ] Verify AWS Credentials
- [ ] Configure Budget Alerts
- [ ] Create AWS SAM Application
- [ ] Create template.yaml
- [ ] Deploy Initial Stack
- [ ] Verify Lambda
- [ ] Verify API Gateway
- [ ] Verify DynamoDB

Deliverable:

Working AWS Infrastructure

---

## Sprint 2 — Backend Foundation

### Tasks

- [ ] Lambda Handler
- [ ] Request Validation
- [ ] Logging Framework
- [ ] Configuration Loader
- [ ] Exception Handling

Deliverable:

Working Backend Skeleton

---

## Sprint 3 — Investigation Engine

### Tasks

- [ ] Incident Engine
- [ ] Log Parser
- [ ] Noise Filter
- [ ] Prompt Builder
- [ ] Response Builder

Deliverable:

Incident processing pipeline

---

## Sprint 4 — AI Provider Layer

### Tasks

- [ ] AI Provider Interface
- [ ] Mock AI Provider
- [ ] Bedrock Provider
- [ ] Configuration Switch
- [ ] JSON Validation

Deliverable:

AI abstraction layer

---

## Sprint 5 — Database Layer

### Tasks

- [ ] DynamoDB Repository
- [ ] Save Investigation
- [ ] Retrieve Investigation
- [ ] List Investigations

Deliverable:

Persistent storage

---

## Sprint 6 — REST APIs

### Tasks

- [ ] POST /investigate
- [ ] GET /incidents
- [ ] GET /incidents/{id}
- [ ] Error Responses
- [ ] Input Validation

Deliverable:

Complete REST API

---

## Sprint 7 — Frontend

### Tasks

- [ ] React Project
- [ ] Upload Page
- [ ] Investigation Report
- [ ] Incident History
- [ ] API Integration

Deliverable:

Working Dashboard

---

## Sprint 8 — Deployment

### Tasks

- [ ] Deploy using AWS SAM
- [ ] Deployment Script
- [ ] Cleanup Script
- [ ] Verify Cloud Deployment

Deliverable:

Production MVP

---

# Phase 1.5 — AI Evaluation Framework

## Goal

Measure AI quality before introducing Retrieval-Augmented Generation.

---

## Sprint 9 — Evaluation Dataset

### Tasks

- [ ] Create 50 Sample Incidents
- [ ] Label Ground Truth
- [ ] Store Dataset

Deliverable:

Evaluation Dataset

---

## Sprint 10 — Evaluation Engine

### Tasks

- [ ] Accuracy Measurement
- [ ] Precision
- [ ] Recall
- [ ] Hallucination Detection
- [ ] Latency Measurement
- [ ] Cost Measurement

Deliverable:

Evaluation Framework

---

# Phase 2 — Retrieval-Augmented Generation (RAG)

## Goal

Enable historical incident retrieval.

---

## Sprint 11 — Embeddings

### Tasks

- [ ] Titan Embeddings
- [ ] Embedding Storage
- [ ] Embedding Generator

Deliverable:

Embeddings Pipeline

---

## Sprint 12 — Vector Search

### Tasks

- [ ] FAISS Integration
- [ ] Similar Incident Search
- [ ] Ranking

Deliverable:

Local Vector Database

---

## Sprint 13 — Retrieval Pipeline

### Tasks

- [ ] Context Retrieval
- [ ] Prompt Enrichment
- [ ] Improved AI Analysis

Deliverable:

RAG Pipeline

---

## Sprint 14 — Benchmarking

### Tasks

- [ ] Compare Without RAG
- [ ] Compare With RAG
- [ ] Generate Metrics

Deliverable:

Performance Report

---

# Phase 3 — Production Engineering

## Goal

Transform the MVP into a production-inspired system.

---

## Sprint 15 — Monitoring

### Tasks

- [ ] CloudWatch Logs
- [ ] Metrics
- [ ] Dashboard

Deliverable:

Observability

---

## Sprint 16 — CI/CD

### Tasks

- [ ] GitHub Actions
- [ ] Automated Tests
- [ ] Automated Deployment

Deliverable:

CI/CD Pipeline

---

## Sprint 17 — Analytics

### Tasks

- [ ] Cost Dashboard
- [ ] Latency Dashboard
- [ ] Evaluation Dashboard

Deliverable:

Operational Analytics

---

# Final Phase — Portfolio Preparation

## Tasks

- [ ] Complete README
- [ ] Architecture Diagram
- [ ] Sequence Diagram
- [ ] API Documentation
- [ ] Screenshots
- [ ] Demo Video
- [ ] Resume Bullet Points
- [ ] LinkedIn Project Write-up
- [ ] GitHub Release

---

# Success Criteria

The project is considered complete when:

- [ ] Serverless architecture is fully functional.
- [ ] AI generates structured incident reports.
- [ ] Historical investigations are stored.
- [ ] Evaluation framework reports measurable metrics.
- [ ] RAG improves investigation quality.
- [ ] CI/CD pipeline is operational.
- [ ] Complete documentation is published.
- [ ] GitHub repository is portfolio-ready.
- [ ] AWS costs remain within the ₹1000 budget.

---

# Progress Tracker

| Phase | Progress |
|--------|----------|
| Project Setup | ██████████ 100% |
| MVP | ░░░░░░░░░░ 0% |
| Evaluation | ░░░░░░░░░░ 0% |
| RAG | ░░░░░░░░░░ 0% |
| Production | ░░░░░░░░░░ 0% |
| Portfolio | ░░░░░░░░░░ 0% |

---

# Notes

- Develop locally using Mock AI whenever possible to minimize AWS costs.
- Deploy to AWS only when validating functionality or recording demonstrations.
- Destroy cloud resources after testing to stay within the project budget.
- Keep documentation synchronized with implementation throughout development.