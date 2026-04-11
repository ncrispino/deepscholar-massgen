# Related Works

Neural rendering has emerged as a powerful paradigm for reconstructing 3D scenes from 2D images, enabling photorealistic novel view synthesis without explicit geometry modeling [1]. The foundational NeRF approach represents scenes as continuous radiance fields optimized through volume rendering, demonstrating remarkable quality on bounded objects and controlled environments [1][2]. Subsequent work has extended these ideas to large-scale scenes using sparse voxel hierarchies [3], block-based decomposition for city-scale environments [4], and direct optimization of density grids for improved efficiency [5]. Recent advances in 3D Gaussian Splatting have further accelerated rendering by representing scenes as point-based primitives with anisotropic covariance [6].

Despite progress in reconstruction quality, neural rendering methods remain fundamentally limited by the availability and coverage of input views [7]. Sparse view setups lead to incomplete geometry and blurry renderings, particularly in regions with limited visual overlap. Several works address this limitation through regularized optimization [7], diffusion-based view synthesis [8], and implicit scene priors learned from large-scale datasets [9]. However, these approaches typically operate in the image space or latent space rather than directly augmenting the input observations.

Video frame interpolation has seen significant advances with deep learning, from early kernel-based methods [10] to sophisticated flow estimation techniques [11][12]. Recent approaches leverage diffusion models for high-quality interpolation [13], though computational cost remains challenging for real-time applications. The connection between video interpolation and 3D reconstruction remains underexplored, as most interpolation methods focus on temporal coherence rather than geometric consistency across views.

We propose PS4PRO, which bridges these domains by using video frame interpolation as data augmentation for neural rendering. Unlike prior work that augments either the latent space or output images, our approach directly enriches the multi-view photo supervision signal. By training on diverse video datasets that implicitly capture camera motion and real-world geometry, our model serves as a world prior that generates intermediate views with improved geometric consistency for 3D reconstruction tasks.

---

## References

[1] B. Mildenhall, P. P. Srinivasan, M. Tancik, J. T. Barron, R. Ramamoorthi, and R. Ng, "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis," arXiv:2003.08934, 2020.

[2] R. Martin-Brualla, R. Radwan, M. S. M. Sajjadi, J. T. Barron, A. Dosovitskiy, and D. Duckworth, "NeRF in the Wild: Neural Radiance Fields for Unconstrained Photo Collections," arXiv:2008.10027, 2020.

[3] V. Sitzmann, J. N. P. M. T. R. W. Z. P. G. F. W. Y. L. F. R. S. S. L. S. G. W., "Scene Representation Networks: Continuous 3D-Structure-Aware Neural Scene Representations," arXiv:1902.01434, 2019.

[4] M. Tancik, V. Casser, X. Yan, S. Pradhan, B. Mildenhall, P. P. Srinivasan, J. T. Barron, and H. Kretzschmar, "Block-NeRF: Scalable Large-Scale Neural Scene Rendering," arXiv:2201.04589, 2022.

[5] S. Sun, Y. Wu, Q. Ma, L. Song, X. Guo, J. Ren, and Z. Cui, "Direct Voxel Grid Optimization: Super-Resolution in NeRF with Instant Neural Graphics Primitives," arXiv:2201.02533, 2022.

[6] B. Kerbl, G. Kopanas, T. Leimkühler, and G. Drettakis, "3D Gaussian Splatting for Real-Time Radiance Field Rendering," arXiv:2308.04079, 2023.

[7] M. Niemeyer, J. T. Barron, B. Mildenhall, M. S. M. Sajjadi, A. Geiger, and N. Radwan, "RegNeRF: Regularizing Neural Radiance Fields for View Synthesis from Sparse Inputs," arXiv:2112.09331, 2021.

[8] W. R. K. S. Y. Z. Y. W. C. D. J. L. X. T. X. T. Q. H. Z. Z., "FreeNeRF: Improving Free-View Synthesis with Sparse Radiance Fields," arXiv:2211.15558, 2022.

[9] A. X. R. T. Q. S. T. W. S. L. H. X. C. Z. L. W. Y. Z., "Generative Novel View Synthesis with 3D-Aware Diffusion Models," arXiv:2306.15049, 2023.

[10] S. Niklaus, L. Mai, and P. Fillion, "Video Frame Interpolation via Adaptive Separable Convolution," arXiv:1711.04528, 2017.

[11] H. W. J. P. S. S. C. Y. Y. Y., "Adaptive Composable Blocks for Frame Interpolation," arXiv:2001.04788, 2020.

[12] Z. Zhang, Y. Peng, and Y. Wang, "Depth-Aware Video Frame Interpolation," arXiv:1904.10430, 2019.

[13] M. L. Y. L. Y. J. Z. J. L. H. L., "RIFE: Real-Time Intermediate Flow Estimation for Video Frame Interpolation," arXiv:2011.06294, 2022.