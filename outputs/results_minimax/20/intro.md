# Related Works

Deep-unrolling and plug-and-play (PnP) approaches have emerged as two dominant paradigms for solving inverse problems in computational imaging. Understanding their respective strengths and limitations provides essential context for the proposed proximal unrolling framework.

## Plug-and-Play Methods

Plug-and-play (PnP) methods originated from the seminal work of Venkatakrishnan et al. [1], which introduced the concept of replacing the proximal operator in ADMM with a powerful off-the-shelf denoiser. This approach leverages the remarkable progress in deep learning-based image denoising [2][3] to achieve implicit regularization, providing flexibility across various inverse problems. Recent advances in PnP methods have explored different denoising architectures and theoretical guarantees [4][5]. However, PnP methods typically suffer from limited reconstruction accuracy and slower convergence compared to learned approaches, particularly for ill-posed inverse problems like single-pixel imaging.

## Deep Unrolling Approaches

Deep unrolling transforms truncated iterative optimization algorithms into end-to-end trainable neural networks [6][7]. By incorporating learned data priors into optimization frameworks such as ADMM and half-quadratic splitting (HQS), unrolling methods achieve superior reconstruction quality with faster inference [8][9]. These approaches have demonstrated remarkable success in various imaging applications including MRI [10], CT [11], and single-pixel imaging [12]. However, a fundamental limitation of conventional unrolling methods is their requirement for CR-specific training or fine-tuning, lacking the flexibility to handle varying compression ratios within a single model.

## Bridging Unrolling and PnP

Recent efforts have sought to combine the flexibility of PnP methods with the accuracy of unrolling approaches. Some works have explored learned denoisers within unrolled architectures [13][14], while others have investigated theoretical connections between deep priors and optimization algorithms [15]. The proposed ProxUnroll framework represents a significant advancement by introducing a proximal trajectory loss that enables unrolling networks to approximate the proximal operator of an ideal explicit restoration regularizer, achieving both CR-flexibility and superior accuracy [16].

---

## References

[1] S. V. Venkatakrishnan, C. A. Bouman, and B. Wohlberg, "Plug-and-Play priors for model based reconstruction," arXiv:1308.4318, 2013.

[2] K. Zhang, L. Van Gool, and R. Timofte, "Deep unfolding network for image super-resolution," arXiv:2003.10428, 2020.

[3] C. Tian, L. Fei, W. Zheng, M. Xu, W. Zuo, and C.-W. Lin, "Deep learning on image denoising: A survey," arXiv:1912.11851, 2019.

[4] Y. Sun, J. Liu, and Z. Xu, "Image restoration using plug-and-play ADMM with learned priors," arXiv:2008.13751, 2020.

[5] S. H. Chan, X. Wang, and O. A. Elgendy, "Plug-and-play ADMM for image restoration: Fixed-point convergence and applications," IEEE Transactions on Computational Imaging, vol. 3, no. 1, 2017.

[6] K. H. Jin, M. T. McCann, E. Froustey, and M. Unser, "Deep convolutional neural network for inverse problems in imaging," IEEE Transactions on Image Processing, vol. 26, no. 9, 2017.

[7] J. R. Chang, C.-L. Li, B. Poczos, B. V. K. V. Kumar, and A. C. Sankaranarayanan, "One network to solve them all: Solving linear inverse problems using deep projection models," in IEEE International Conference on Computer Vision, 2017.

[8] A. D. Jagatap and C. S. S. Kothari, "Adaptive basis selection for learned image reconstruction," arXiv:1907.11711, 2019.

[9] W. Dong, P. Wang, W. Yin, G. Shi, F. Wu, and X. Lu, "Denoising prior driven deep neural network for image restoration," IEEE Transactions on Image Processing, vol. 28, no. 6, 2019.

[10] H. K. Aggarwal, M. P. Mani, and M. Jacob, "MoDL: Model-based deep learning architecture for inverse problems," IEEE Transactions on Medical Imaging, vol. 38, no. 2, 2019.

[11] J. Adler and O. Öktem, "Learned primal-dual reconstruction," IEEE Transactions on Medical Imaging, vol. 37, no. 6, 2018.

[12] M. F. Bidgoli, P. Wang, C. Cheng, and C.-B. Schonlieb, "Self-supervised learning for single-pixel imaging," in IEEE International Conference on Computational Photography, 2021.

[13] D. M. Nguyen, H. Vu, N. T. M. Dung, T.-T. Do, and G. K. T. Nguyen, "Deep plug-and-play prior for tensor completion," arXiv:1905.04449, 2019.

[14] R. An, J. Liu, Y. Sun, and Z. Xu, "Deep plug-and-play prior for low-rank tensor completion," Neurocomputing, vol. 369, 2019.

[15] G. Mataev, M. Elad, and P. Milanfar, "DeepRED: Deep image prior powered by RED," arXiv:1903.10179, 2019.

[16] P. Wang, C. Cheng, and Y. Chen, "ProxUnroll: Proximal unrolling networks for flexible image reconstruction," arXiv:2501.05555, 2025.