# ADR-002: Why DynamoDB

**Status:** Accepted

## Context

The application needs persistent storage for investigation reports.

Candidate databases:

- DynamoDB
- PostgreSQL
- MongoDB

---

## Decision

Amazon DynamoDB was selected.

---

## Rationale

Reasons include:

- Fully managed
- Serverless
- Pay-per-request pricing
- Automatic scaling
- Native AWS integration
- Suitable for JSON-style documents

The application's access patterns are simple and map well to DynamoDB.

---

## Consequences

### Advantages

- No server management
- Cost-effective
- High availability
- Scalable

### Disadvantages

- Different data modeling approach than relational databases
- Joins are not supported

---

## Future Considerations

Global Secondary Indexes (GSIs) may be introduced as new query patterns emerge.