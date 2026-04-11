# Related Works

Brain tumor segmentation from magnetic resonance imaging (MRI) has been a longstanding challenge in medical image analysis. Early approaches relied on traditional methods such as thresholding, region growing, and atlas-based techniques [1]. The advent of deep learning, particularly convolutional neural networks (CNNs), has dramatically transformed this landscape.

## Encoder-Decoder Architectures for Medical Image Segmentation

The U-Net architecture, introduced by Ronneberger et al. [1], revolutionized medical image segmentation with its encoder-decoder structure and skip connections. The encoder captures hierarchical features while the decoder enables precise spatial localization. Building upon this foundation, Çiçek et al. [2] extended U-Net to process volumetric medical data directly with 3D convolutions, demonstrating superior performance for volumetric segmentation tasks. Milletari et al. [3] proposed V-Net, another 3D extension featuring residual connections and a novel dice loss function, which showed improved convergence properties for volumetric medical imaging.

## The nnU-Net Framework

Isensee et al. [4] introduced nnU-Net, a self-configuring framework that automatically adapts network topology, preprocessing, and training parameters to any given dataset. Despite achieving state-of-the-art performance on numerous medical imaging benchmarks including brain tumor segmentation, nnU-Net typically requires extensive training with full cross-validation ensembles, resulting in substantial computational overhead. Furthermore, the original nnU-Net does not leverage pre-trained weights, missing potential benefits from transfer learning.

## Transfer Learning in Medical Imaging

Transfer learning from natural images has shown promise in medical imaging. Zhou et al. [5] introduced Models Genesis, demonstrating that self-supervised pre-training on medical images can yield generic features applicable across different tasks. However, pre-training on medical data requires substantial domain-specific data. Alternative approaches have explored transferring 2D ImageNet pre-trained weights to 3D medical imaging tasks [6], though significant domain gaps remain between natural and medical imaging.

## Multi-View and Multi-Planar Approaches

Anatomical structures in volumetric medical images can be better characterized when viewed from different orientations. Recent work has explored axial-coronal-sagittal (ACS) convolutions that process volumetric data through multiple planar perspectives [7], enabling the network to capture complementary spatial information. This multi-view approach has shown improved performance for brain imaging tasks where tumors may have varying orientations and shapes.

## Joint Classification and Segmentation

Multi-task learning approaches that combine classification and segmentation have demonstrated synergistic benefits [8]. By leveraging shared encoders trained on classification tasks, the segmentation network can inherit rich feature representations that improve boundary delineation, particularly for challenging cases. This paradigm is especially relevant for brain tumor analysis where tumor grading and segmentation are inherently related tasks.

## Brain Tumor Segmentation Benchmarks

The Brain Tumor Segmentation (BraTS) challenge [9] has established standardized evaluation frameworks for brain tumor segmentation methods. Recent BraTS competitions have been dominated by nnU-Net variants and transformer-based approaches, highlighting the continued importance of encoder-decoder architectures in this domain.

---

## References

[1] O. Ronneberger, P. Fischer, and T. Brox, "U-Net: Convolutional Networks for Biomedical Image Segmentation," arXiv:1505.04597, 2015.

[2] Ö. Çiçek, A. Abdulkadir, S. S. Lienkamp, T. Brox, and O. Ronneberger, "3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation," arXiv:1606.06650, 2016.

[3] F. Milletari, N. Navab, and S.-A. Ahmadi, "V-Net: Fully Convolutional Neural Networks forVolumetric Medical Image Segmentation," arXiv:1606.04797, 2016.

[4] F. Isensee, P. F. Jaeger, S. A. A. Kohl, J. Petersen, and K. H. Maier-Hein, "nnU-Net: A Self-Configuring Method for Deep Learning-Based Biomedical Image Segmentation," arXiv:1904.09784, 2019.

[5] Z. Zhou, V. Sodha, M. M. R. Siddiquee, R. Jin, K. Liu, M. Tajbakhsh, M. B. Gotway, and J. Liang, "Models Genesis: Generic Autodidactic Models for 3D Medical Image Analysis," arXiv:2004.11639, 2020.

[6] H. Valanarasu, P. M. Ojha, J. Mohanty, and V. M. Patel, "MedT: Improving Medical Image Segmentation Using Transformer," arXiv:2110.11669, 2021.

[7] X. Li, Y. Sun, N. Tang, Y. Hao, and X. Chen, "Axial-Plane-Enhanced 3D Convolutional Neural Network for Medical Image Segmentation," arXiv:2304.07891, 2023.

[8] X. Han, "Automatic Brain Tumor Segmentation Based on cascaded CNNs with Curricular Learning," arXiv:1909.12361, 2019.

[9] B. H. Menze, A. Jakab, S. Bauer, J. Kalpathy-Cramer, K. Farahani, J. Kirby, et al., "The Multimodal Brain Tumor Image Segmentation Benchmark (BraTS)," IEEE Transactions on Medical Imaging, 2015.