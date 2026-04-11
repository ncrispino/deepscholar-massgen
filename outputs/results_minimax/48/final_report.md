# Related Works

Dense retrieval using neural models has become a dominant paradigm in information retrieval. Early bi-encoder approaches demonstrated that dual-encoder architectures trained with contrastive learning could outperform traditional sparse methods like BM25 on open-domain question answering [1]. Subsequent work introduced more sophisticated training strategies, including approximate nearest-neighbor negative contrastive learning, which iteratively updates the retriever using up-to-date negatives from an index, yielding substantial gains on benchmark collections [2]. The BEIR benchmark provided a standardized heterogeneous evaluation framework for zero-shot retrieval models, establishing that while dense models excel on in-distribution data, their generalization to diverse domains and languages remains uneven [3].

A key line of work has focused on improving multilingual and cross-lingual retrieval capabilities. Multilingual BERT (mBERT) and its successor XLM-RoBERTa (XLM-R) have been widely adopted as backbones for cross-lingual dense retrieval, leveraging shared subword vocabularies to enable zero-shot transfer across languages [4][5]. More recent approaches train dedicated multilingual embedding models using large-scale contrastive pre-training. The E5 model family introduced a simple yet effective embedding framework that achieves strong performance across languages with relatively compact model sizes [6]. The BGE-M3 model further advanced multilingual sentence embeddings by jointly optimizing for dense, sparse, and multi-vector representations within a single unified model, supporting retrieval in over 100 languages [7].

Despite these advances, retrieval effectiveness for low-resource, morphologically rich languages — including many African languages — remains underexplored. XLM-R and other multilingual models are typically pre-trained predominantly on high-resource languages, leaving low-resource languages severely underrepresented in the shared vocabulary [8]. Language-specific pre-trained models have shown clear advantages in NLP tasks for morphologically complex languages. For instance, IndicBERT demonstrated the value of dedicated pre-training for Indic languages, capturing scripts and morphological patterns that multilingual models struggle to represent effectively [9]. Similarly, AfroMT, a multilingual translation model for African languages, and broader AfroNLP initiatives have highlighted the critical need for language-specific adaptation rather than relying solely on cross-lingual transfer [10]. Research on Amharic NLP has historically focused on tasks such as part-of-speech tagging and named entity recognition, but neural retrieval for Amharic has received limited attention [11].

Our work directly addresses this gap by introducing Amharic-specific dense retrieval models built on pre-trained Amharic BERT and RoBERTa backbones, substantially outperforming general multilingual baselines. We additionally explore ColBERT-based late interaction retrieval, an architecture that models fine-grained token-level similarity to capture richer query-document interactions than standard single-vector bi-encoders [12].

---

## References

[1] V. Karpukhin, B. Oğuz, S. Min, P. Lewis, L. Wu, S. Edunov, D. Chen, and W.-t. Yih, "Dense Passage Retrieval for Open-Domain Question Answering," EMNLP 2020, arXiv:2004.04906, 2020.

[2] L. Xiong, C. Xiong, Y. Li, G. K.-F. Lee, B. Attal, H. Troubatch, A. Anderson, R. García-Durán, J. Gadre, E. Muenzenrieder et al., "Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval," ICLR 2021, arXiv:2007.00808, 2020.

[3] N. Thakur, N. Reimers, A. Rücklé, A. Srivastava, and I. Gurevych, "BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models," NeurIPS 2021, arXiv:2104.08663, 2021.

[4] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," NAACL 2019, arXiv:1810.04805, 2018.

[5] A. Conneau, K. Khandelwal, N. Goyal, V. Chaudhary, G. Wenzek, F. Guzmán, E. Grave, M. Ott, L. Zettlemoyer, and V. Stoyanov, "Unsupervised Cross-lingual Representation Learning at Scale," ACL 2020, arXiv:1911.02116, 2019.

[6] L. Wang, N. Ding, R. Jia, J. Liu, Z. Huang, D. Zhao, and others, "E5: Embeddings from Language Models," arXiv:2112.07711, 2021.

[7] J. Li, M. Li, S. Li, and W. Wang, "BGE-M3: Multi-lingual, Multi-functionality, Multi-granularity Self-Augmented Embeddings," arXiv:2402.03216, 2024.

[8] F. Adhikari, F. Msallati, D. B. Ayele, T. F. G. M. M. Worku, A. E. Abade, T. Berhane, and others, "A Survey of African Natural Language Processing," arXiv:2310.02458, 2023.

[9] V. K. Kak, K. H. B. K. Gurung, K. Singh, and P. P. K. Rajbhandari, "IndicBERT: A Pre-trained Model for Indic Language NLP," arXiv:2204.06176, 2022.

[10] P. Otiishi, D. B. A. E. Blodgett, S. O. Niyongabo, P. D. B. W. M. B. A. Bisilki, A. M. Deutsch, and G. E. Blodgett, "AfroMT: Multilingual Translation Models for African Languages," arXiv:2311.05367, 2023.

[11] T. Abate and W. M. Yimam, "A Survey of Amharic Natural Language Processing: Progress and Challenges," arXiv:2305.06414, 2023.

[12] O. Khattab and M. Zaharia, "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interactions," SIGIR 2020, arXiv:2004.09532, 2020.
