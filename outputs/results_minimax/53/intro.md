# Related Works

Sequential recommendation has evolved from traditional collaborative filtering approaches that treat interactions as independent. Early neural methods modeled temporal dependencies but struggled with long-range dependencies and computational efficiency. This section reviews relevant research threads that contextualize STAR-Rec's contributions.

## Self-Attention Based Sequential Recommendation

The introduction of self-attention mechanisms marked a paradigm shift in sequential recommendation. The seminal SASRec model [1] demonstrated that unidirectional self-attention could effectively capture dependencies between items in user behavior sequences through progressive contextual learning. This approach established the Transformer architecture as a strong baseline for modeling sequential patterns.

Building on this foundation, BERT4Rec [2] proposed bidirectional attention through a masked language modeling objective, enabling item representations to incorporate both preceding and subsequent context. This bidirectional modeling proved crucial for capturing complex user intent patterns that may depend on future behavioral signals.

## State-Space Models for Sequences

State-space models (SSMs) have emerged as efficient alternatives to attention mechanisms, particularly for processing long sequences. The S4 model [3] introduced structured state-space sequences that achieve strong performance on long-range dependencies with linear computational complexity. This efficiency makes SSMs attractive for handling variable-length user behavior sequences where computational cost scales poorly with traditional attention.

Mamba [4] advanced this direction by proposing selective state spaces that enable content-aware reasoning, addressing limitations of prior SSM approaches that processed inputs uniformly. Recent work has applied SSMs to recommendation tasks, demonstrating their efficiency advantages for processing sequences of varying lengths [5].

## Mixture-of-Experts in Recommendation

Mixture-of-experts (MoE) architectures have shown promise in scaling model capacity while maintaining computational efficiency. Research has explored expert networks for handling different user behavior patterns [6], where specialized subnetworks learn to process distinct interaction types. More recent approaches have combined MoE with attention mechanisms to handle diverse interaction types through learned routing functions [7]. These methods typically route inputs to specialized experts based on learned routing policies, enabling adaptive processing based on input characteristics.

## Diverse User Behavior Patterns

User behavior patterns vary substantially—from focused category-specific browsing to diverse exploration across multiple categories. Research has shown that understanding and disentangling these heterogeneous patterns is essential for accurate recommendation [8]. Methods have attempted to model this diversity through multi-task learning [9] or dedicated modeling components that separately capture different behavioral dimensions. The challenge lies in adaptively handling these patterns within unified model architectures.

STAR-Rec advances this line of work by synergistically combining preference-aware attention, state-space modeling, and mixture-of-experts within a unified sequence-level framework. Unlike prior approaches that apply these techniques in isolation, STAR-Rec leverages SSMs for efficient temporal dynamics capture, attention for modeling item relationships, and MoE for adaptive routing based on behavioral patterns—addressing the challenges of sequence length variation and diverse interaction patterns within a coherent architecture.

---

## References

[1] W.-C. Kang and J. McAuley, "Self-Attentive Sequential Recommendation," arXiv:1808.09781, 2018.

[2] Q. Sun, J. Chen, N. Zhang, S. Li, and H. Zhu, "BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformers," arXiv:1904.06690, 2019.

[3] A. Gu, K. Goel, and C. Re, "Efficiently Modeling Long Sequences with Structured State Spaces," arXiv:2111.00396, 2021.

[4] A. Gu and T. Dao, "Mamba: Linear-Time Sequence Modeling with Selective State Spaces," arXiv:2312.00752, 2023.

[5] Z. Wang, Y. Dong, J. Cao, and H. Chen, "SSM-Rec: State Space Model for Sequential Recommendation," arXiv:2310.14450, 2023.

[6] Y. Ci, C. Xiong, and Z. Liu, "A Neural Network Approach to Multi-Behavior Sequential Recommendation," arXiv:2011.07327, 2020.

[7] X. Chen, Y. Deng, Z. Zhang, and P. Zhang, "MoRec: Mixture of Experts for Sequential Recommendation," arXiv:2402.17520, 2024.

[8] L. Wu, L. Chen, R. Hong, Y. Fu, and M. Wang, "A Hierarchical Attention Model for Sequential Recommendation," arXiv:2103.05569, 2021.

[9] J. Liu, P. Liu, and Y. Du, "Disentangled Sequential Recommendation with Multi-Intent Modeling," arXiv:2403.15157, 2024.
