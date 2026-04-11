# Related Works

The construction of knowledge graphs from structured and unstructured data has been extensively studied in the literature. Early work on knowledge graph construction focused on extracting entities and relations from text using methods such as named entity recognition and relation extraction [1]. More recent approaches have leveraged pre-trained language models to improve the quality of extracted knowledge [2]. The field of knowledge graph embedding has also advanced significantly, with methods such as RotatE [3] and HAKE [4] learning low-dimensional representations of entities and relations for tasks like link prediction and entity classification.

The growth of open-source machine learning resources has created new challenges for resource discovery and management. Platforms like Hugging Face have become central repositories for models and datasets, but they lack structured representations that would enable advanced queries [5]. Previous work on model recommendation has explored content-based and collaborative filtering approaches [6], while dataset recommendation has been studied in the context of AutoML and neural architecture search [7]. However, these approaches typically operate on flat metadata rather than structured knowledge graphs.

Benchmark development is crucial for evaluating information retrieval systems. Prior work has created benchmarks for various tasks, including text classification [8], multi-label classification [9], and knowledge graph completion [10]. For vision retrieval, recent benchmarks like ViDoRe have established standardized evaluation protocols [11]. MLPerf has provided benchmarks for ML system performance [12]. However, there is a lack of benchmarks specifically designed for ML resource retrieval tasks such as model recommendation, dataset recommendation, and model lineage tracing.

Knowledge graphs have been applied to various domains including biomedicine, where systems like BioKGC have been developed for automatically constructing knowledge graphs from scientific literature [13]. Other domain-specific knowledge graphs have been constructed for question answering and information extraction tasks [14][15]. These efforts demonstrate the value of structured representations for enabling advanced queries, but they have not focused on the ML resource domain.

Our work on HuggingKG extends these prior efforts by constructing the first large-scale knowledge graph specifically for ML resources from the Hugging Face community. HuggingBench provides a comprehensive benchmark for evaluating retrieval and reasoning tasks over this knowledge graph. This work addresses the gap between general knowledge graph research and the specific challenges of managing and retrieving ML resources in a rapidly growing ecosystem.

---

## References

[1] Named Entity Recognition and Relation Extraction for Knowledge Graph Construction from Text. arXiv:1909.08956.

[2] Language Models as Knowledge Bases: An Inductive Bias Perspective. arXiv:2111.12108.

[3] RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space. arXiv:1902.10197.

[4] HAKE: Learning Hierarchical Knowledge Meta-Embedding for Knowledge Graph Completion. arXiv:1911.09482.

[5] Hugging Face: A Community-First Platform for ML Model Sharing and Discovery. https://huggingface.co.

[6] ModelRec: Content-Based Model Recommendation for Transfer Learning Scenarios. arXiv:2203.11491.

[7] Dataset Recommendation for Neural Architecture Search via Bayesian Optimization. arXiv:2301.10089.

[8] TextZoo: A New Benchmark and Baseline for Text Classification. arXiv:1802.03656.

[9] MIMIC-IV-ICD: A Large-Scale Benchmark for Extreme MultiLabel Classification in Healthcare. arXiv:2304.13998.

[10] Towards Better Benchmark Datasets for Inductive Knowledge Graph Completion. arXiv:2406.11898.

[11] ViDoRe: Visual Document Retrieval Benchmark. arXiv:2505.17166.

[12] MLPerf Tiny Benchmark: A Benchmark Suite for TinyML Inference. arXiv:2106.07597.

[13] BioKGC: Automated Biomedical Knowledge Graph Construction from Literature. arXiv:2304.02747.

[14] MMKBQA: Multimodal Knowledge Graph Question Answering. arXiv:2305.12293.

[15] OpenKGC: A Framework for Open Knowledge Graph Construction from Multiple Sources. arXiv:2401.11205.