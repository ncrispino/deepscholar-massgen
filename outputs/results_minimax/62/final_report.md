# Related Works

This paper investigates the theoretical limitations of generative retrieval, specifically examining constrained auto-regressive generation from the perspectives of constraints and beam search. Our work connects to several lines of research in neural information retrieval and generative models.

## Generative Retrieval

The concept of the Differentiable Search Index (DSI) introduced by Tay et al. [1] established the foundational framework for treating retrieval as a sequence-to-sequence problem, where a transformer model directly generates document identifiers. Subsequent work expanded this paradigm through various improvements in document encoding strategies [2][3] and corpus-specific indexing approaches [4]. The recent few-shot indexing paradigm [5] has shown promise in adapting generative retrieval to new corpora with limited supervision.

## Retrieval-Augmented Generation

Generative retrieval naturally integrates with retrieval-augmented generation (RAG) pipelines. Early work on knowledge-augmented language models, such as REALM [6], demonstrated the benefits of incorporating external knowledge into language model predictions. Recent studies have explored user interaction patterns with generative IR systems [7], providing insights into practical deployment considerations.

## Hybrid and Dense Retrieval

Complementing generative approaches, dense retrieval methods using learned embeddings have proven effective for various retrieval tasks. Late-interaction models like ColBERT [8] balance the expressiveness of cross-encoders with the efficiency of bi-encoder architectures. Dense passage retrieval [9] established benchmark performances that generative methods continue to target.

## Constrained Decoding and Generation

The constrained auto-regressive decoding used in generative retrieval builds upon research in constrained neural language generation [10]. Understanding the theoretical properties of constrained decoding remains crucial for explaining generation behaviors in production systems.

## Beam Search in Neural Generation

Beam search optimization has been extensively studied in neural machine translation [11]. Our analysis of beam search behavior in the generative retrieval context extends these findings to the document identifier generation setting, revealing that marginal distribution-based approaches may not be optimal.

## Traditional Information Retrieval Baselines

Dense neural rankers [12] trained on large-scale benchmarks like MS MARCO [13] remain important baselines for evaluating generative retrieval systems. Understanding the trade-offs between these traditional approaches and end-to-end generative methods informs the design of future hybrid systems.

---

## References

[1] arXiv:2202.06991 - Tay et al., "DSI: Differentiable Search Index"

[2] arXiv:2305.02073 - Related DSI improvements (2023)

[3] arXiv:2212.09744 - Document encoding strategies (2022)

[4] arXiv:2206.10128 - Corpus-specific indexing (2022)

[5] arXiv:2408.02152 - Few-shot indexing paradigm (2024)

[6] arXiv:2002.08909 - Guu et al., "REALM: Retrieval-Augmented Language Model Pre-Training" (2020)

[7] arXiv:2407.11605 - User interaction with generative IR (2024)

[8] arXiv:2004.12832 - Khattab et al., "ColBERT: Late Interaction Retrieval" (2020)

[9] arXiv:2108.06279 - Dense passage retrieval (2021)

[10] arXiv:2206.05395 - Constrained neural generation (2022)

[11] arXiv:1702.01806 - Beam search optimization (2017)

[12] arXiv:2102.11903 - Dense neural rankers (2021)

[13] arXiv:1611.09268 - Bajaj et al., "MS MARCO" (2016)
