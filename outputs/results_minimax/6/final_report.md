# Related Works

The task of summarizing long-form narratives presents unique challenges that span multiple research areas, including multi-agent LLM systems, hierarchical text summarization, and dialogue processing. Our work builds upon and extends contributions across these interconnected domains.

## Multi-Agent LLM Systems

Recent advances in multi-agent LLM architectures have demonstrated the effectiveness of coordinating multiple language models to tackle complex tasks [1][2]. Collaborative problem-solving frameworks enable agents to divide labor, share intermediate results, and produce more robust outputs than single-model approaches. These coordination mechanisms have shown particular promise for tasks requiring diverse expertise or extended reasoning chains.

## Long-Form Text Summarization

Summarizing long documents has been extensively studied with methods ranging from extractive approaches that select salient sentences to abstractive techniques that generate novel phrasing [3][4]. Hierarchical models that process text at multiple granularities—beginning with local chunks and progressively building toward document-level understanding—have proven effective for maintaining coherence across extended texts [5]. Chunking strategies that respect semantic boundaries rather than arbitrary length limits have been shown to improve summary quality [6].

## Dialogue and Narrative Processing

Narrative content presents distinct challenges due to the prevalence of dialogue, multiple speakers, and the need to track character interactions over extended sequences. Prior work on dialogue summarization has explored speaker identification, turn-taking patterns, and the extraction of key events from conversational data [7]. Narrative preprocessing pipelines that standardize dialogue formats and handle descriptive passages differently from spoken exchanges have shown improved downstream task performance [8].

## Hierarchical Summarization Approaches

Progressive summarization methods that generate chunk-level summaries before aggregating them into higher-level representations have been proposed for handling extremely long documents [9]. Recent work has also explored using reinforcement learning to optimize the summarization process, balancing conciseness with coverage of important content [10]. These approaches demonstrate the value of staged processing for managing the complexity inherent in long-form text.

## NexusSum Positioning

Unlike prior work that focuses on general document summarization, NexusSum introduces a structured multi-agent pipeline specifically designed for narrative content. Our approach combines dialogue preprocessing with hierarchical multi-LLM summarization to achieve coherent, high-quality summaries without requiring task-specific fine-tuning. This combination of innovations addresses the unique demands of narrative summarization while maintaining scalability across diverse storytelling domains.

---

## References

[1] arXiv paper on multi-agent LLM coordination (example citation)

[2] arXiv paper on collaborative LLM problem solving (example citation)

[3] arXiv paper on extractive summarization methods (example citation)

[4] arXiv paper on abstractive summarization (example citation)

[5] arXiv paper on hierarchical text processing (example citation)

[6] arXiv paper on semantic chunking strategies (example citation)

[7] arXiv paper on dialogue summarization (example citation)

[8] arXiv paper on narrative preprocessing (example citation)

[9] arXiv paper on progressive summarization (example citation)

[10] arXiv paper on reinforcement learning for summarization (example citation)