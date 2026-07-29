# Coding Standards

# AIOps Investigator

**Version:** 1.0

**Status:** Active

---

# Purpose

This document defines the coding standards, conventions, and best practices followed throughout the AIOps Investigator project.

Following these standards ensures that the codebase remains consistent, maintainable, readable, and scalable.

---

# Table of Contents

1. General Principles
2. Python Standards
3. Project Structure
4. Naming Conventions
5. Type Hints
6. Documentation Standards
7. Logging Standards
8. Error Handling
9. Configuration Management
10. Git Workflow
11. Commit Message Convention
12. Testing Standards
13. Security Standards
14. Code Review Checklist

---

# 1. General Principles

- Write readable code before clever code.
- Keep functions small and focused.
- Follow the Single Responsibility Principle.
- Avoid code duplication.
- Prefer composition over inheritance.
- Every module should have a clear purpose.

---

# 2. Python Standards

- Follow PEP 8.
- Use Black for formatting.
- Use Ruff for linting.
- Maximum line length: 100 characters.
- Use Python 3.12 features only.

---

# 3. Project Structure

Each folder has a single responsibility.

- handlers → Lambda entry points
- services → Business logic
- providers → AI providers
- repositories → Database access
- validators → Validation logic
- models → Data models
- utils → Shared utilities
- tests → Unit and integration tests

Business logic must never be placed inside Lambda handlers.

---

# 4. Naming Conventions

## Files

snake_case.py

Example:

incident_engine.py

---

## Classes

PascalCase

Example:

IncidentEngine

---

## Functions

snake_case

Example:

analyze_incident()

---

## Variables

snake_case

Example:

incident_report

---

## Constants

UPPER_CASE

Example:

MAX_LOG_SIZE

---

# 5. Type Hints

Every public function must include type hints.

Example

def analyze(logs: str) -> IncidentReport:

Avoid using `Any` unless absolutely necessary.

---

# 6. Documentation Standards

Every public class and function should include a docstring.

Use Google-style docstrings.

Example

Args:
Returns:
Raises:

---

# 7. Logging Standards

Never use print().

Always use the logging module.

Levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Do not log:

- AWS credentials
- API keys
- Sensitive customer data

---

# 8. Error Handling

Raise meaningful exceptions.

Avoid broad `except Exception`.

Validate inputs before processing.

Return structured error responses.

---

# 9. Configuration Management

Never hardcode:

- AWS Region
- Table Names
- Model IDs
- Secrets

Use configuration files or environment variables.

---

# 10. Git Workflow

Main Branch

main

Feature Branches

feature/<feature-name>

Example

feature/mock-provider

---

# 11. Commit Message Convention

Use Conventional Commits.

Examples

feat: add incident parser

fix: validate AI response schema

docs: update architecture

test: add parser tests

refactor: simplify repository layer

---

# 12. Testing Standards

Every new feature should include tests.

Preferred structure:

- Unit tests
- Integration tests

Target coverage:

≥80%

---

# 13. Security Standards

- Never commit secrets.
- Validate all user input.
- Follow least-privilege IAM.
- Use HTTPS in production.
- Store secrets outside source code.

---

# 14. Code Review Checklist

Before merging:

- Code builds successfully.
- Tests pass.
- Linting passes.
- Type hints added.
- Documentation updated.
- No hardcoded secrets.
- Error handling implemented.
- Logging added where appropriate.