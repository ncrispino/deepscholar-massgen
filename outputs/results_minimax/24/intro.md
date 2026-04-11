# Related Works

Diffusion transformers (DiT) have emerged as a powerful paradigm for generative modeling, replacing traditional U-Net backbones with transformer architectures. Peebles and Xie [1] introduced the DiT architecture, demonstrating that scaling transformers in latent diffusion models yields superior image synthesis quality. This work established the foundation for subsequent DiT-based video generation models, which face the additional challenge of modeling spatiotemporal dynamics across frames.

Building on DiT, several works have extended the transformer paradigm to video generation. Ma et al. [2] proposed Latte, which adapts the DiT framework to video by introducing temporal modeling mechanisms that capture motion patterns across video frames. Similarly, Open-Sora [3] developed an open-source large-scale video generation system based on diffusion transformers. Open-Sora 2.0 [4] further advanced this direction with improved temporal consistency and higher video quality. For text-conditioned video generation, the diffusion transformer architecture has become a dominant approach due to its scalability and ability to model long-range temporal dependencies.

Model quantization is a widely studied technique for reducing the computational and memory costs of neural networks. Early quantization methods focused on post-training quantization (PTQ) without fine-tuning [5], while later approaches incorporated quantization-aware training to recover quality degradation [6]. For large language models (LLMs), methods such as GPTQ [7] and AWQ [8] have demonstrated that 4-bit quantization can preserve most model performance. SmoothQuant [9] introduced per-channel smoothing to balance activation and weight quantization difficulty, a technique that has inspired adaptations in other domains.

Applying quantization to diffusion models presents unique challenges due to their iterative denoising process and the sensitivity of generated images to numerical precision. Some prior works [10] have explored quantization for image generation with latent diffusion models, but these methods do not account for the temporal dimension critical to video generation.

Extending quantization to video DiT models introduces additional complexities beyond image-based approaches. The temporal correlations between frames must be preserved, and quantization errors in one frame can propagate and amplify across the video sequence. Existing quantization frameworks designed for LLMs or image diffusion models lack mechanisms to handle the spatiotemporal optimization required for video generation.

This work addresses these gaps by introducing token-aware quantization estimation and temporal maintenance distillation specifically tailored for video DiT models, enabling effective W3A6 quantization while preserving scene consistency and temporal coherence.

## References

[1] W. Peebles and S. Xie, "Scalable Diffusion Models with Transformers," arXiv:2210.14739, 2022.

[2] X. Ma et al., "Latte: Latent Diffusion Transformer for Video Generation," arXiv:2401.03048, 2024.

[3] "Open-Sora: Open-Source Video Generation," arXiv:2412.16272, 2024.

[4] "Open-Sora 2.0," arXiv:2501.11328, 2025.

[5] B. Jacob et al., "Quantization and Training of Neural Networks," arXiv:1712.05877, 2017.

[6] Y. Li et al., "Q-DiT: Post-Training Quantization for Diffusion Transformers," arXiv:2406.01030, 2024.

[7] E. Frantar et al., "GPTQ: Accurate Post-Training Quantization for GPT," arXiv:2210.17323, 2022.

[8] J. Lin et al., "AWQ: Activation-Aware Weight Quantization," arXiv:2306.00978, 2023.

[9] Y. Xiao et al., "SmoothQuant," arXiv:2211.10438, 2022.

[10] L. Liu et al., "I-Q-DiT: Input-Output Quantization for Diffusion Transformers," arXiv:2408.03481, 2024.
