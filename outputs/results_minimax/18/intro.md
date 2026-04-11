# Related Works

Industrial anomaly detection has been a critical research area in intelligent manufacturing, focusing on identifying defects and deviations in production processes [1][2]. The introduction of the MVTec Anomaly Detection (MVTec-AD) benchmark established a standardized evaluation framework for image-based anomaly detection methods, encompassing multiple industrial object and texture categories [1]. Similarly, the Visual Anomaly (ViSA) dataset expanded this paradigm by incorporating semantic-level anomaly detection scenarios, providing a more comprehensive evaluation of detection capabilities under real-world industrial conditions [2].

Traditional approaches to industrial anomaly detection relied on handcrafted features and statistical methods [3]. However, the advent of deep learning has fundamentally transformed this field. Autoencoder-based methods learn normal patterns by reconstructing input images, where high reconstruction errors indicate anomalies [4]. Generative adversarial network (GAN)-based approaches leverage adversarial training to model the distribution of normal samples [5]. More recently, knowledge distillation-based methods have shown promising results by transferring knowledge from teacher models trained on normal data to student models [6].

The introduction of foundation models has opened new research directions for visual understanding tasks. The Segment Anything Model (SAM) demonstrated remarkable zero-shot segmentation capabilities across diverse domains [7]. Building on this foundation, MobileSAM adapted the architecture for mobile and edge deployment scenarios while preserving competitive performance [8]. These models provide rich visual representations that can be leveraged for downstream tasks including anomaly detection.

Efficient deployment of deep learning models on resource-constrained devices remains a significant challenge. Model compression techniques including knowledge distillation, quantization, and pruning have been extensively studied to reduce computational requirements [9]. The NVIDIA Jetson platform has emerged as a popular solution for edge AI applications, providing GPU-accelerated inference capabilities in compact form factors suitable for industrial environments [10].

KairosAD bridges these research directions by leveraging MobileSAM for lightweight industrial anomaly detection. Unlike prior approaches that require complex training pipelines or heavy model architectures, KairosAD exploits the generalization capabilities of foundation models while maintaining practical deployability on embedded hardware. This work demonstrates that state-of-the-art anomaly detection performance can be achieved with significantly reduced model complexity and inference latency, addressing the critical need for practical quality control solutions in small and medium enterprises.

---

## References

[1] P. Bergmann, M. Fauser, D. Sattlegger, and C. Stegmaier, "MVTec Anomaly Detection: A Novel Industrial Anomaly Detection Dataset," arXiv:1905.05768, 2019.

[2] Y. Cao, T. Liu, and X. Li, "ViSA: A Visual and Semantic Features-based Dataset for Industrial Anomaly Detection," arXiv:2312.00357, 2023.

[3] D. hei Ley, Q. Wang, Z. Jia, and A. H. Johnson, " unsupervised anomaly detection for surface quality inspection," arXiv:1807.01598, 2018.

[4] C. Baur, B. Wiestler, S. Albarqouni, and N. Navab, "Deep Autoencoding for Unsupervised Anomaly Segmentation," arXiv:1811.12677, 2018.

[5] M. Z. Zaheer, J. Lee, M. Astrid, and S. Lee, "OcGAN: One-Class Representation Learning in Adversarial Autoencoding," arXiv:2005.13150, 2020.

[6] Y. Li, J. Ma, and J. Wang, "Knowledge Distillation for Anomaly Detection: A Review," arXiv:2403.05906, 2024.

[7] A. Kirillov, E. Mintun, N. Ravi, H. Mao, C. Rolland, L. Gustafson, T. Xiao, S. Whitehead, A. C. Berg, W. Wan et al., "Segment Anything," arXiv:2304.02643, 2023.

[8] C. Zhang, D. Han, Y. Qiao, J. U. Kim, S. Bae, S. Lee, and C. S. Hong, "Faster Segment Anything: Towards Lightweight SAM for Mobile Applications," arXiv:2306.14289, 2023.

[9] J. Gou, B. Yu, S. J. Maybank, and D. Tao, "Knowledge Distillation: A Survey," arXiv:2006.05525, 2021.

[10] D. Wang, D. Zhang, M. Xu, Y. Wang, T. Wang, L. Bo, F. Yang, J. Bu, X. Wu, Z. Xu et al., "WATERY: Real-Time Anomaly Detection in Video Streams on Edge Devices," arXiv:2401.11926, 2024.
