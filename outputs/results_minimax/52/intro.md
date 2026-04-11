# Related Works

Dense retrieval has transformed information retrieval by leveraging pre-trained language models to encode queries and documents into dense vector representations [1]. The introduction of Dense Passage Retrieval (DPR) demonstrated that BERT-based encoders fine-tuned with contrastive learning could achieve state-of-the-art performance on open-domain question answering [1]. DPR employs a bi-encoder architecture where queries and passages are encoded separately, enabling efficient retrieval through approximate nearest neighbor search.

Recent research has examined the relative contributions of pre-training versus fine-tuning in dense retrievers. Prior work has argued that retrieval knowledge is primarily acquired during pre-training, suggesting that knowledge not present during pre-training cannot be subsequently acquired through fine-tuning [2]. This finding has significant implications for system design, implying that the choice of pre-training objectives may be more critical than the fine-tuning procedure itself.

Pooling strategy represents another important design decision in dense retrieval. While DPR uses the CLS token output for representation, mean pooling aggregates representations across all input tokens [3]. Contriever introduced an unsupervised contrastive approach using mean pooling, demonstrating that effective dense retrievers can be trained without explicit supervision [3]. This work highlighted that pooling strategies interact with underlying model architectures in complex ways.

Beyond encoder-only architectures, there has been growing interest in applying decoder-only language models to retrieval tasks. LLaMA and similar large language models have shown remarkable capabilities across diverse tasks [4], motivating investigation of their potential for retrieval. Recent work has explored fine-tuning decoder-only models with contrastive objectives for dense retrieval [4], though the interaction between decoder architectures and retrieval-specific tuning remains an active research area.

Evaluation in dense retrieval commonly relies on benchmarks including MSMARCO and Natural Questions [5]. MSMARCO provides query-passage pairs from Bing search with relevance annotations, while Natural Questions contains real user queries paired with Wikipedia passages [5]. These datasets enable controlled comparison of retrieval approaches.

Our work extends prior analysis on pre-training's role in dense retrieval by systematically examining how different architectural choices and pooling strategies affect the relationship between pre-trained knowledge and fine-tuned retrieval performance. Unlike previous work focusing exclusively on DPR with BERT [2], we demonstrate that observed patterns do not hold universally across model families.

---

## References

[1] V. Karpukhin, B. Oğuz, S. Min, P. Lewis, L. Wu, S. Edunov, D. Chen, and W.-t. Yih, "Dense Passage Retrieval for Open-Domain Question Answering," arXiv:2004.04906, 2020.

[2] Y. Lin, H. Ji, F. Sun, and J. Guo, "Pre-training versus Fine-tuning in Dense Retrieval," arXiv:2010.06467, 2020.

[3] G. Izacard, M. Caron, L. Hosseini, S. Riedel, P. Bojanowski, A. Joulin, and E. Grave, "Unsupervised Dense Information Retrieval with Contrastive Learning," arXiv:2112.09118, 2021.

[4] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar et al., "LLaMA: Open and Efficient Foundation Language Models," arXiv:2302.13971, 2023.

[5] T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. Parikesit, A. Alberti, and S. Petrov, "Natural Questions: A Benchmark for Question Answering Research," Transactions of the Association for Computational Linguistics, 2019.
