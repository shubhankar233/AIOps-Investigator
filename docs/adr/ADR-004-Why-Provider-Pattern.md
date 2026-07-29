# ADR-004: Why Provider Pattern

**Status:** Accepted

## Context

The system needs to support multiple AI providers without modifying business logic.

---

## Decision

Introduce an AI Provider interface.

```
Incident Engine
      │
      ▼
AI Provider Interface
      │
 ┌────┴─────┐
 ▼          ▼
Mock     Bedrock
```

---

## Rationale

Benefits include:

- Loose coupling
- Easier testing
- Better maintainability
- Future extensibility

Business logic depends on an abstraction rather than a concrete implementation.

---

## Consequences

### Advantages

- Easy provider replacement
- Supports dependency inversion
- Cleaner architecture

### Disadvantages

- Slightly more initial code
- Additional abstraction layer

---

## Future Considerations

Additional providers (OpenAI, Anthropic, Azure OpenAI) can be added with minimal changes.