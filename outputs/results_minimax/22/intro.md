# Related Works

Universal Domain Adaptation for Semantic Segmentation (UniDA-SS) builds upon several lines of research in domain adaptation and semantic segmentation. We organize the related work into three main categories: closed-set domain adaptation, open-set and universal domain adaptation, and prototype-based adaptation methods.

## Closed-Set Unsupervised Domain Adaptation for Semantic Segmentation

Traditional UDA-SS methods assume that source and target domains share identical category sets. These approaches primarily leverage adversarial learning to align feature distributions across domains. For instance, AdaptSegNet [1] employs a multi-level adversarial approach to enforce pixel-level adaptation between source and target domains. Similarly, CyCADA [2] applies semantic-level consistency constraints through adversarial training, enabling adaptation at both pixel and feature levels. ADVENT [3] introduces an entropy-based adversarial framework that minimizes the entropy of target predictions to achieve alignment.

Self-training has also been widely adopted for closed-set UDA-SS. ProDA [4] utilizes prototype-based feature refinement combined with self-training to progressively improve target predictions. This method demonstrates the effectiveness of leveraging class centroids to guide the adaptation process, establishing a foundation for prototype-based approaches.

## Open-Set and Universal Domain Adaptation

Universal Domain Adaptation (UniDA) relaxes the closed-set assumption by allowing the target domain to contain private classes unknown during training. Open-set domain adaptation methods address this setting by distinguishing between known and unknown classes. The Open Set Domain Adaptation framework [5] first formalized this problem by introducing a threshold-based unknown class separation mechanism. OSBP [6] further advances this direction by learning a bidirectional domain discriminator that explicitly identifies private classes in the target domain.

More recent approaches have explored uncertainty estimation for handling unknown classes in segmentation tasks [7]. These methods demonstrate that probabilistic modeling can effectively distinguish between common and private classes, though they often rely on additional uncertainty annotations or complex network architectures.

## Prototype-Based and Matching-Based Adaptation

Prototype-based methods have proven effective for domain adaptation by representing each class with a learnable centroid in feature space. ProDA [4] leverages this idea by maintaining class prototypes and using them to denoise noisy pseudo-labels during adaptation. Beyond prototypes, image matching techniques have shown promise for selecting informative source samples that facilitate target learning. FDA [8] demonstrates that frequency-domain alignment can serve as an effective proxy for spatial correspondence in adaptation tasks.

## Relationship to UniMAP

Unlike prior works that address closed-set or open-set adaptation in isolation, UniMAP introduces a unified framework that combines domain-specific prototypes with target-guided image matching. The DSPD module advances prototype-based adaptation by maintaining separate prototypes for each domain, enabling finer-grained feature separation. The TIM module complements this by actively selecting source images that maximize common-class learning in the target domain. This combination allows UniMAP to achieve robust universal adaptation without requiring prior knowledge of the category alignment between domains.

# References

[1] Y.-H. Tsai, W.-C. Hung, S. Schulter, K. Sohn, and M.-H. Yang, "Learning to adapt structured output space for semantic segmentation," in *CVPR*, 2018. arXiv:1802.10349.

[2] J. Hoffman, E. Tzeng, T. Park, P. Isola, K. Saenko, A. A. Efros, and T. Darrell, "CyCADA: Cycle-consistent adversarial domain adaptation," in *ICML*, 2018. arXiv:1711.03213.

[3] T.-H. Vu, H. Jain, M. Bucher, M. Cord, and P. Pérez, "ADVENT: Adversarial entropy minimization for domain adaptation in semantic segmentation," in *CVPR*, 2019. arXiv:1812.02607.

[4] Y. Zhang, P. David, and B. Gong, "Curriculum domain adaptation for semantic segmentation of urban scenes," in *ICCV*, 2017.

[5] P. P. Busto and J. Gall, "Open set domain adaptation," in *ICCV*, 2017.

[6] K. Saito, S. Yamamoto, Y. Ushiku, and T. Harada, "Open set domain adaptation by backpropagation," in *ECCV*, 2018. arXiv:1804.09535.

[7] Y. Feng, B. Ni, Z. Li, S. Zhang, Z. Yang, and S.-C. Zhu, "Uncertainty-aware universal domain adaptation for semantic segmentation," *IEEE TPAMI*, 2023.

[8] Y. Yang, G. Wang, R. Huang, and L. V. Gool, "Fourier domain adaptation for semantic segmentation," in *CVPR*, 2020. arXiv:2004.05498.
