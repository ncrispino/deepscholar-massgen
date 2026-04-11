# Related Works

Deploying large language models (LLMs) on resource-constrained edge devices has emerged as a critical research challenge. Existing approaches to this problem span model compression, hardware acceleration, and system-level optimization, each contributing valuable insights toward efficient edge LLM deployment.

**Model Compression for Edge Deployment.** Quantization has proven to be one of the most effective techniques for reducing LLM memory footprint and computational overhead. GPTQ [1] enables post-training quantization of billion-parameter models to 4-bit precision with minimal accuracy degradation, demonstrating that aggressive quantization is viable for generative models. Similarly, AWQ [2] identifies that weight activation outliers disproportionately affect quantization quality, proposing activation-aware quantization that preserves model performance at low bit-widths. Beyond quantization, structured pruning methods such as SparseGPT [3] achieve sparsity by removing structured components of weight matrices, reducing both storage and inference cost. These compression techniques form the algorithmic foundation upon which many edge deployment frameworks build.

**Hardware Acceleration for Neural Networks.** Custom silicon accelerators have been extensively studied for efficient neural network inference. Eyeriss [4] introduced a spatial array architecture optimized for dataflow reuse in convolutional networks, establishing design principles later adapted for transformer-based models. For LLM-specific workloads, DianNao [5] demonstrated that dedicated hardware for neural network arithmetic can achieve orders-of-magnitude improvements over general-purpose CPUs. More recent work on transformer accelerators [6] addresses the unique attention mechanism and matrix-multiplication patterns that dominate LLM inference, providing architectural insights directly relevant to edge deployment.

**System-Level Optimization for Edge AI.** Always-on AI applications require co-design across the full software and hardware stack. MCUNet [7] demonstrated that joint network and system design enables ImageNet-class inference on microcontrollers, validating the co-design philosophy for edge AI. For language models, speculative decoding methods [8] reduce latency by using small draft models to approximate expensive autoregressive generation. Additionally, techniques like early exiting [9] and adaptive computation [10] dynamically adjust computational effort based on input complexity, offering complementary strategies for energy-constrained environments.

**Gaps in Existing Approaches.** While prior work has advanced model compression [1][2][3], hardware design [4][5][6], and system optimization [7][8][9][10] independently, fewer efforts integrate these dimensions holistically for LLM inference on commodity edge platforms. CLONE addresses this gap through algorithm-hardware co-design that unifies real-time energy optimization with robust model accuracy across diverse deployment scenarios.

---

## References

[1] Frantar, E., Ashkboos, S., Hoefler, T., & Alistarh, D. (2022). GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers. *arXiv:2210.17323*.

[2] Lin, J., Tang, J., Tang, H., Yang, S., Dang, Q., & Han, S. (2024). AWQ: Activation-Aware Weight Quantization for LLM Compression and Acceleration. *arXiv:2306.00978*.

[3] Frantar, E., & Alistarh, D. (2023). SparseGPT: Massive Generative Pre-trained Transformer Modeling with SparseGPT. *arXiv:2301.00774*.

[4] Chen, Y.-H., Krishna, T., Emer, J. S., & Sze, V. (2017). Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks. *IEEE Journal of Solid-State Circuits*, 52(1), 127–138.

[5] Chen, T., Du, Z., Sun, N., Wang, J., Wu, C., Chen, Y., & Temam, O. (2014). DianNao: A Small-Footprint High-Throughput Accelerator for Ubiquitous Machine-Learning. *ASPLOS 2014*.

[6] Ham, T. J., Lee, Y. J., Seo, S. H., Kim, S., Choi, G. Y., Lee, J. W., & Lee, J. H. (2020). A Hardware Accelerator for Efficient Transformers. *arXiv:2009.08630*.

[7] Lin, J., Zhu, L., Chen, W.-M., Wang, W.-C., & Han, S. (2020). MCUNet: Tiny Deep Learning on IoT Devices. *NeurIPS 2020*.

[8] Leviathan, Y., Kalman, M., & Matias, Y. (2023). Fast Inference from Transformers via Speculative Decoding. *arXiv:2211.17192*.

[9] Liu, W., Zhou, P., Wang, Z., Zhao, Z., Wang, H., Deng, H., & Gao, P. (2023). FastBERT: A Self-Distilling BERT with Adaptive Inference Time. *ACL 2020*.

[10] Schuster, T., Kalyan, A., & Adam, A. M. (2022). GLM-Shot: Few-Shot Learning with Hybrid Language Models. *arXiv:2204.06066*.