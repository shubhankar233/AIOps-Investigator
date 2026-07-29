# ADR-006: Why Local FAISS Instead of OpenSearch

**Status:** Accepted

## Context

Version 2 introduces semantic search for historical incident retrieval.

Potential solutions:

- Amazon OpenSearch Serverless
- Amazon Bedrock Knowledge Bases
- Local FAISS

---

## Decision

Use Local FAISS during development.

---

## Rationale

Reasons include:

- No recurring cloud infrastructure cost
- Fits within the ₹1000 project budget
- Fast local experimentation
- Easy migration to managed services later

For the expected project dataset (tens to hundreds of incidents), FAISS provides sufficient performance.

---

## Consequences

### Advantages

- Very low cost
- Fast local searches
- Simple setup
- Excellent for prototyping

### Disadvantages

- Not distributed
- Manual index management
- Limited scalability compared to managed vector databases

---

## Future Considerations

If the project grows beyond prototype scale, migration to Amazon OpenSearch Serverless or another managed vector database can be evaluated.