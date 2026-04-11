# Related Works

## Attention and Memory Optimization

Significant research has focused on optimizing the attention mechanism in Transformers to reduce computational and memory costs. FlashAttention [1] and its improved version FlashAttention-2 [2] revolutionized attention computation by using tiling and fusion techniques to reduce memory footprint from quadratic to linear complexity while maintaining numerical accuracy. These optimizations directly benefit KV cache systems by enabling more efficient processing of cached key-value pairs during inference.

## LLM Serving Systems

Efficient serving of large language models has been a critical research area. Orca [3] pioneered iteration-level scheduling for LLM serving, allowing fine-grained control over request processing. The vLLM system [4] introduced paged attention, a technique that manages the KV cache like virtual memory pages, significantly improving throughput and memory utilization. These systems provide the foundational infrastructure upon which KV cache optimization strategies are built.

## Speculative Decoding

Speculative decoding methods leverage KV cache reuse to accelerate inference. SpecInfer [5] uses a tree-based speculative execution paradigm where multiple candidate tokens are generated and verified in parallel. Medusa [6] extends this approach by adding multiple prediction heads to generate continuations simultaneously. Both approaches rely heavily on KV cache reuse patterns to achieve speedups, making workload characterization essential for their effective deployment.

## KV Cache Characterization and Eviction

Prior work has explored cache management for LLM inference. Existing eviction policies in serving systems [4] typically use simple heuristics like LRU. However, these approaches were developed based on synthetic workloads or limited production traces. The research community has lacked comprehensive characterization of real-world KV cache access patterns from production environments. Our work addresses this gap by providing the first systematic analysis of KV cache workload patterns from a leading LLM service provider, revealing insights that differ substantially from synthetic workload assumptions.

---

## References

[1] Dao, T., et al. "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness." arXiv:2205.14135, 2022.

[2] Dao, T. "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning." arXiv:2307.08691, 2023.

[3] Yu, G.-I., et al. "Orca: A Distributed Serving System for Transformer-Based Generative Models." OSDI 2022. arXiv:2201.11788.

[4] Kwon, W., et al. "Efficient Memory Management for Large Language Model Serving with PagedAttention." SOSP 2023. arXiv:2309.06180.

[5] Chen, C., et al. "SpecInfer: Accelerating Large Language Model Serving with Tree-based Speculative Inference." arXiv:2305.09719, 2023.

[6] Cai, T., et al. "Medusa: Simple Framework for Accelerating LLM Generation with Multiple Decoding Heads." arXiv:2311.06296, 2023.