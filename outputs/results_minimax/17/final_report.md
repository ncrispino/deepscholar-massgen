# Related Works

Semi-supervised learning (SSL) has emerged as a powerful paradigm for leveraging unlabeled data alongside limited labeled examples. Early seminal works established the foundation for modern SSL techniques. Temporal ensembling [1] and Mean Teacher [6] introduced consistency regularization, where models are trained to produce similar predictions for differently perturbed versions of the same input. MixMatch [3] unified multiple SSL heuristics including consistency regularization and entropy minimization. FixMatch [2] further advanced the field by combining pseudo-labeling with consistency regularization, achieving remarkable performance with simplified pipelines.

A fundamental assumption underlying conventional SSL methods is that labeled and unlabeled data are drawn from the same class distribution [5]. This assumption, however, is frequently violated in real-world applications where unlabeled datasets inevitably contain unknown classes or outliers. Oliver et al. [5] provided a realistic evaluation of SSL methods, demonstrating that performance degrades substantially when this assumption is violated. This problem, known as open-set semi-supervised learning, has gained increasing attention as practitioners recognize that real-world data rarely conforms to the closed-world assumption.

Existing approaches to handling outliers in SSL can be categorized into confidence-based methods and data-driven approaches. Confidence-based methods typically rely on a single model's prediction confidence to identify potential outliers, trusting high-confidence predictions and treating low-confidence ones as uncertain or out-of-distribution. Chen et al. [4] proposed using uncertainty estimation for open-set SSL, leveraging the model's confidence to distinguish between known and unknown classes. Li et al. [7] introduced DivideMix, which jointly addresses noisy labels and semi-supervised learning by dynamically dividing the training data based on prediction confidence. Self-training approaches such as Noisy Student [8] leverage large unlabeled datasets with noisy labels by iteratively filtering out potentially incorrect pseudo-labels. Confident Learning [9] provides a principled framework for identifying mislabeled examples and outliers by analyzing prediction probabilities.

A critical limitation shared by these prior methods is their reliance on a single model's predictions for outlier detection [4][7][8]. When labeled data is scarce, a single model may lack sufficient discriminative power to reliably distinguish inliers from outliers. This paper's proposed Diversify and Conquer (DAC) framework addresses this limitation by exploiting prediction disagreements among multiple differently-biased models. By constructing a collection of heads that are diversely biased toward the unlabeled distribution through a single training process, DAC leverages inter-model disagreement as a robust signal for identifying unknown concepts, even when the labeled data is underspecified.

---

## References

[1] S. Laine and T. Aila. Temporal ensembling for semi-supervised learning. *arXiv:1610.02242*, 2016.

[2] K. Sohn, D. Berthelot, N. Carlini, Z. Zhang, H. Zhang, C. A. Raffel, E. D. Cubuk, A. Kurakin, and C.-L. Li. FixMatch: Simplifying semi-supervised learning with consistency and pseudo-labeling. *arXiv:2001.07685*, 2020.

[3] D. Berthelot, N. Carlini, I. Goodfellow, N. Papernot, A. Oliver, and C. A. Raffel. MixMatch: A holistic approach to semi-supervised learning. *arXiv:1905.02249*, 2019.

[4] J. Chen, Y. Li, G. Liu, Z. Huang, and J. Yin. Open-set semi-supervised learning with uncertain representation. *arXiv:2103.09470*, 2021.

[5] A. Oliver, A. Odena, C. A. Raffel, E. D. Cubuk, and I. Goodfellow. Realistic evaluation of deep semi-supervised learning algorithms. *arXiv:1703.03400*, 2017.

[6] A. Tarvainen and H. Valpola. Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results. *arXiv:1703.01780*, 2017.

[7] J. Li, R. Socher, and S. C. H. Hoi. DivideMix: Learning with noisy labels as semi-supervised learning. *arXiv:2002.08597*, 2020.

[8] Q. Xie, M.-T. Luong, E. Hovy, and Q. V. Le. Self-training with noisy student improves ImageNet classification. *arXiv:1911.04252*, 2019.

[9] C. Northcutt, L. Jiang, and I. Chuang. Confident learning: Estimating uncertainty in dataset labels. *arXiv:1911.09781*, 2019.
