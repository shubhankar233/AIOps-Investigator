# ADR-005: Why Repository Pattern

**Status:** Accepted

## Context

Direct database access inside business logic leads to tight coupling and difficult testing.

---

## Decision

Introduce a Repository layer between the Incident Engine and DynamoDB.

```
Incident Engine
      │
      ▼
Incident Repository
      │
      ▼
DynamoDB
```

---

## Rationale

The Repository Pattern separates persistence logic from business logic.

This improves:

- Maintainability
- Testability
- Code organization

---

## Consequences

### Advantages

- Cleaner architecture
- Easier mocking during tests
- Database implementation can change independently

### Disadvantages

- Additional abstraction layer

---

## Future Considerations

Alternative storage implementations can be introduced without changing the Incident Engine.