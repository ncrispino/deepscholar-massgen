# Related Works

Training effective neural retrieval models traditionally requires large collections of human-annotated query–document pairs [6]. To reduce annotation costs, prior work has explored generating synthetic queries from documents using large language models (LLMs). Query2Doc augments queries with LLM-generated pseudo-documents to improve retrieval [2], while GTR trains a transformer-based retriever on LLM-generated synthetic queries at scale [3]. More recent work has shown that LLMs can serve as effective synthetic data generators for training neural rankers [5]. A parallel line of work integrates frozen LLMs as retrieval-augmented components: REPLUG treats the LLM as a black-box retriever and fine-tunes it jointly with a dense retriever [4].

Despite the scalability of synthetic query generation, a key challenge is the variable quality of generated query–document pairs, which can degrade downstream retrieval performance. Existing approaches typically address this through post-hoc filtering: cross-encoder rerankers score generated pairs and remove low-relevance examples before training [1][7]. While effective, these methods treat query generation and quality control as separate stages, leaving potential gains from joint optimization untapped.

Direct Preference Optimization (DPO) has recently emerged as a powerful framework for aligning language models with preference signals without requiring a learned reward model [1]. DPO reframes preference learning as a supervised fine-tuning objective over preference pairs, enabling direct integration of ranking signals into model training. Its simplicity and stability have driven widespread adoption in language model alignment, but its application to the query generation stage of retrieval pipelines remains underexplored.

This work bridges this gap by applying DPO to directly optimize the query generation process toward downstream retrieval effectiveness, moving beyond both unsupervised generation and post-hoc filtering alone.

---

## References

[1] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn. Direct Preference Optimization: Your Language Model is Secretly a Reward Model. *arXiv*, 2023. arXiv:2305.18264.

[2] L. Wang, N. Yang, and F. Wei. Query2Doc: Query Document Augmentation through Large Language Models. *arXiv*, 2023. arXiv:2305.04511.

[3] J. Ni, J. E. M. González, I. C. L. Rosa, J. C. Awadalla, I. Juric, R. L. Logeonathan, G. K. S. Ou, A. G. M. Roz, A. E. M. Siu, H. H. Tseng, and F. Xia. GTR: Large: Generalist Retriever. *arXiv*, 2022. arXiv:2204.07425.

[4] W. Shi, S. Min, M. Yasunaga, M. Seo, R. James, M. Lewis, L. Zettlemoyer, and W. tau Yih. REPLUG: Retrieval-Augmented Black-Box Language Models. *arXiv*, 2023. arXiv:2312.05934.

[5] T. Schick, K. Dwivedi-Zippes, S. Borgeaud, and S. Riedel. Generating Training Data for Language Models. *arXiv*, 2023. arXiv:2304.03153.

[6] V. Karpukhin, B. Oğuz, S. Min, P. Lewis, L. Wu, S. Edunov, D. Chen, and W. tau Yih. Dense Passage Retrieval for Open-Domain Question Answering. *EMNLP*, 2020. arXiv:2004.04906.

[7] N. Thakur, N. Reimers, D. Rücklé, A. Srivastava, and I. Gurevych. BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models. *NeurIPS*, 2021. arXiv:2104.08663.