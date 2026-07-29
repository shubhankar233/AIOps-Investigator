# ADR-001: Why AWS SAM

**Status:** Accepted

## Context

The project requires Infrastructure as Code (IaC) for deploying a serverless application consisting of AWS Lambda, API Gateway, and DynamoDB.

Possible options included:

- AWS SAM
- AWS CDK
- Terraform
- Manual Console Deployment

---

## Decision

AWS SAM was selected as the Infrastructure as Code framework.

---

## Rationale

AWS SAM offers:

- Native support for serverless services
- Simple YAML templates
- Local Lambda execution
- Easy deployment
- Easy cleanup
- Minimal configuration
- Strong AWS documentation

It aligns well with the project's goal of learning AWS serverless development.

---

## Consequences

### Advantages

- Fast development
- Easy deployment
- AWS-native tooling
- Simplified local testing

### Disadvantages

- Less flexible than Terraform for multi-cloud environments
- Primarily focused on AWS serverless workloads

---

## Future Considerations

If the project expands to a multi-cloud architecture, Terraform may be evaluated.