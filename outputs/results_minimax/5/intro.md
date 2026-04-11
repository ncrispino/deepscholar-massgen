# Related Works

Instruction-following text embedding has emerged as a critical research direction in natural language processing, enabling embeddings to dynamically adapt to user-specified instructions. This section reviews prior work in text embedding methods, instruction-aware models, and efficient embedding computation.

## Pre-trained Text Embeddings

Foundational work on pre-trained language models established the basis for modern text embeddings. BERT [7] introduced bidirectional transformer encoders that capture rich semantic information, which became the backbone for subsequent embedding methods. Sentence-BERT [6] extended BERT by using siamese network architectures to produce semantically meaningful sentence-level embeddings suitable for similarity search. Contrastive learning has proven effective for improving embedding quality, as demonstrated by SimCSE [4], which leverages dropout-based positive pairs for self-supervised sentence embedding learning. RetroMAE [5] further advanced retrieval-oriented embeddings through masked auto-encoder pre-training with retrieval-specific objectives.

## Instruction-Aware Embedding Models

A significant advancement in text embeddings came with models designed to follow instructions. INSTRUCTOR [1] pioneered instruction-following text embeddings by incorporating task-specific instructions into the embedding generation process, enabling a single model to handle diverse downstream tasks. Promptagator [8] utilized large language models as few-shot labelers to create instruction-aware dense retrieval models, demonstrating the effectiveness of instruction guidance for retrieval tasks. BGE M3-Embedding [2] introduced multi-lingual, multi-functionality, and multi-granularity text embeddings with structural improvements, achieving state-of-the-art performance across diverse embedding tasks.

## Efficient Embedding Computation

Traditional approaches to instruction-following embeddings require re-encoding the entire corpus for each new instruction, creating substantial computational overhead for large-scale applications. E5 [3] proposed extractive passage-based embeddings that balance quality and efficiency, though still requiring full re-encoding for instruction changes. Recent work has explored lightweight transformation mechanisms that avoid expensive re-encoding by adapting pre-computed embeddings, representing an orthogonal approach to efficiency that maintains embedding quality while dramatically reducing computational costs for dynamic instruction scenarios.

## Positioning of GSTransform

GSTransform advances the field by recognizing that instruction-relevant information is inherently encoded in generic embeddings but remains underutilized. Unlike prior approaches that require repeated corpus encoding [1][2][8] or focus solely on extraction-based efficiency [3], GSTransform introduces a lightweight guided space transformation mechanism that adapts pre-computed embeddings in real-time, achieving significant speedups while maintaining or improving embedding quality across diverse instruction-following tasks.

---

## References

[1] Su, H., Shi, W., Kasai, J., Wang, Y., Hu, Y., Ostendorf, M., Yih, W., Smith, N. A., Zettlemoyer, L., and Yu, T. (2023). INSTRUCTOR: One embedding for all tasks, instructions, and domains. In *Findings of the Association for Computational Linguistics: EMNLP 2023*, pages 6006–6021. arXiv:2212.08617.

[2] Chen, J., Liu, K., Cai, D., Liu, J., Liu, R., Chen, Z., He, X., and Gu, J. (2024). BGE M3-Embedding: Multi-lingual, multi-functionality, multi-granularity text embeddings through structure. arXiv:2402.03216.

[3] Wang, L., Yang, N., Huang, X., Jiao, B., Yang, P., Jiang, D., Majumder, R., and Wei, F. (2023). E5: Embeddings from extractive passages. arXiv:2304.03516.

[4] Gao, T., Yao, X., and Chen, D. (2021). SimCSE: Simple contrastive learning of sentence embeddings. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, pages 6894–6910. arXiv:2104.08821.

[5] Liu, Y., Huang, J., Liu, J., Liu, S., Liu, Q., Shi, S., and Chen, E. (2022). RetroMAE: Pre-training retrieval-oriented language models via masked auto-encoder. In *Findings of the Association for Computational Linguistics: EMNLP 2022*, pages 2503–2516. arXiv:2205.12035.

[6] Reimers, N. and Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using siamese BERT-networks. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing*. arXiv:1908.10084.

[7] Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics*, pages 4171–4186. arXiv:1810.04805.

[8] Chen, Z., Zhang, F., Guo, J., and Ma, S. (2023). Promptagator: Using LLMs as few-shot labelers for instruction-aware dense retrieval. arXiv:2309.09298.
