# ADR-003: Why Mock AI Provider

**Status:** Accepted

## Context

Calling Amazon Bedrock during development increases costs and introduces network dependencies.

---

## Decision

Implement a Mock AI Provider for local development.

---

## Rationale

The mock provider enables:

- Offline development
- Predictable outputs
- Faster testing
- Lower AWS costs
- Repeatable unit tests

The business logic remains independent of the actual AI provider.

---

## Consequences

### Advantages

- Near-zero development cost
- Reliable automated tests
- Faster feedback loop

### Disadvantages

- Does not reflect real model behavior
- Cannot evaluate prompt quality

---

## Future Considerations

The mock provider will remain available for testing even after Bedrock integration.