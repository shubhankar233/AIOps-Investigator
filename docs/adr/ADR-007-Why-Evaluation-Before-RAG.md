# ADR-007: Why Evaluation Before Retrieval-Augmented Generation (RAG)

**Status:** Accepted

## Context

Many AI projects introduce Retrieval-Augmented Generation (RAG) without first measuring the baseline performance of the language model.

Without baseline metrics, it is impossible to determine whether RAG genuinely improves the quality of generated results.

---

## Decision

Implement an evaluation framework before integrating RAG.

The project will first measure:

- Root cause accuracy
- Severity classification accuracy
- Response latency
- Cost per investigation
- JSON validation success rate

Only after collecting baseline metrics will RAG be introduced.

---

## Rationale

This approach enables objective comparison between:

- AI without retrieval
- AI with retrieval

The project can demonstrate measurable improvements instead of subjective claims.

---

## Consequences

### Advantages

- Quantifiable improvements
- Better engineering discipline
- Easier experimentation
- More credible portfolio project
- Stronger interview discussions

### Disadvantages

- Additional development effort
- Requires creation of a labeled evaluation dataset

---

## Future Considerations

Future versions may automate regression testing by running the evaluation suite after every major model or prompt update.