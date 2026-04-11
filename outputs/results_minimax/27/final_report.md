# Related Works

Natural language-driven table discovery identifies relevant tables from large repositories based on natural language queries. Our work on Birdie, which employs a differentiable search index to unify indexing and search in a single encoder-decoder model, draws upon several interconnected research areas.

## Dense Vector Search for Table Retrieval

Traditional approaches to table retrieval rely on dense vector search pipelines, following a representation-index-search paradigm [1][2]. These methods encode queries and tables into dense vector representations using bi-encoder or cross-encoder architectures, then retrieve relevant tables through approximate nearest neighbor search. For table-specific retrieval, models such as TURL have advanced the field by learning unified representations of tables, their schemas, and content [3]. However, this pipeline suffers from error accumulation: representation errors compound during indexing and negatively impact search accuracy.

## End-to-End Learned Retrieval

Recent work has explored end-to-end differentiable approaches that unify indexing and retrieval into a single model. The Differentiable Search Index (DSI) framework represents documents directly as parameters within a transformer model, enabling the model to directly generate document identifiers for queries [4]. This paradigm eliminates the traditional pipeline and enables joint optimization of indexing and retrieval. Our Birdie framework extends this direction by adapting the DSI approach to the table discovery domain using prefix-aware identifiers and an encoder-decoder architecture.

## Query Generation for Retrieval

Query generation has proven valuable for improving retrieval systems by creating synthetic training data. Query2Doc leverages large language models to generate pseudo-documents that bridge the gap between queries and target documents [5]. This approach has been extended in subsequent work that explores LLM-based query generation for various retrieval scenarios [6]. Birdie adopts a similar strategy by using an LLM-based query generator to create synthetic queries for tables, which are used to train the unified encoder-decoder model.

## Continual Learning for Dynamic Indexing

A key challenge in real-world retrieval systems is accommodating new tables without catastrophic forgetting of previously indexed data. The Elastic Weight Consolidation (EWC) method addresses this by identifying and protecting important weights during sequential learning [7]. Progressive neural networks offer an alternative by expanding network capacity for new tasks while freezing old parameters [8]. More recent approaches explore parameter isolation strategies that allocate dedicated parameters to different time periods or data batches [9]. Birdie's index update strategy via parameter isolation draws from these foundations, reducing forgetting significantly compared to alternative continual learning approaches.

## References

[1] V. Karpukhin, B. Oguz, S. Min, P. Lewis, L. Wu, S. Edunov, D. Chen, and W.-t. Yih. Dense passage retrieval for open-domain question answering. In *EMNLP*, 2020.

[2] Y. Liu, K. Bai, P. Anand, Y. Song, and J. Gao. Dense vector retrieval with learned representations. In *EMNLP*, 2020.

[3] X. Deng, H. Sun, A. Lees, Y. Wu, and C. Yu. TURL: Table understanding and representation learning. In *ACL*, 2022.

[4] Y. Tay, V. Tran, M. Dehghani, J. Ni, D. Bahri, H. Mei, Z. Zhao, N. Houlsby, and D. K. I. G. Transformer-based indexing for search. In *NeurIPS*, 2022.

[5] B. Wang, S. Wang, Y. Cheng, Z. Tu, P. Liu, and M. R. K. Introducing semantics into retrieval via query2doc. In *ACL*, 2023.

[6] S. Min, J. Lee, Y. Choi, J. Kim, and G. Kim. Synthetic query generation for retrieval using large language models. In *ECIR*, 2023.

[7] J. Kirkpatrick, R. Pascanu, N. Rabinowitz, J. Veness, G. Desjardins, A. A. Rusu, K. Milan, J. Quan, T. Ramalho, and A. Grabska-Barwinska. Overcoming catastrophic forgetting in neural networks. *PNAS*, 2017.

[8] A. A. Rusu, N. C. Rabinowitz, G. Desjardins, H. Soyer, J. Kirkpatrick, K. Kavukcuoglu, R. Pascanu, and R. Hadsell. Progressive neural networks. *arXiv:1606.04671*, 2016.

[9] J. Serra, D. Suris, M. Miron, and A. Karatzoglou. Overcoming catastrophic forgetting with hard attention to the task. In *ICML*, 2018.
