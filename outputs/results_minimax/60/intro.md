# Related Works

Prediction calibration has emerged as a critical research area in machine learning, particularly for deep neural networks that often produce overconfident predictions [1][2]. While significant progress has been made in classifier calibration, the calibration of ranking models remains relatively underexplored. Ranking models typically optimize for relative ordering while overlooking the accuracy of absolute score values, which are essential for downstream applications such as ad bidding and content ranking in industrial systems [3].

## Traditional Calibration Approaches

Classical calibration methods have long been employed to adjust model predictions. Platt scaling applies logistic regression to transform raw logits into well-calibrated probabilities [4]. Isotonic regression uses piece-wise constant functions to learn order-preserving mappings and has been extended with ROC-regularized variants for improved performance [5][6]. Temperature scaling, a simple yet effective method, rescales logits by a learned temperature parameter to align confidence with accuracy [2]. Despite their simplicity and interpretability, these traditional approaches suffer from limited expressiveness, as they rely on fixed transformation forms that cannot capture complex relationships between predictions and true probabilities.

## Neural Network-Based Calibration Methods

Recent research has explored learning-based calibration approaches that leverage the flexibility of neural networks. Mixup-based methods interpolate between training samples to produce smoother decision boundaries and improve calibration [7][8]. Specifically, RankMixup adapts mixup training to the ranking domain by interpolating both inputs and their ranking scores, demonstrating that ranking-based mixup strategies can enhance network calibration beyond standard classification settings [9]. Other work has investigated joint optimization of input perturbation and temperature scaling through neural clamping techniques [10][11].

## Monotonic Constraints in Neural Networks

A fundamental challenge in calibration is maintaining the order-preserving property: calibrated scores should preserve the relative ordering of original predictions. This monotonicity constraint ensures that items ranked higher remain ranked higher after calibration. The Unconstrained Monotonic Neural Network (UMNN) framework provides a principled approach to learning arbitrary monotonic functions while maintaining great modeling power [12]. By parameterizing the derivative of the monotonic function using a neural network, UMNN enables flexible monotonic transformations that can be integrated into larger learning pipelines.

## Calibration in Ranking Systems

Ranking model calibration presents unique challenges due to the interdependence of scores across items. The SortNet framework demonstrates how neural networks can learn to rank by adapting sorting algorithms [13]. However, most existing ranking calibration methods apply post-hoc transformations with fixed functional forms, limiting their ability to handle complex calibration scenarios encountered in large-scale industrial applications [3]. Recent approaches have begun exploring adaptive calibration methods that can adjust to the specific characteristics of ranking distributions [11].

## Loss Functions for Calibration

Training-time calibration approaches directly optimize for calibration quality through custom loss functions. Mixup-based calibration loss functions have shown theoretical connections between mixup training and improved calibration, with conditions under which mixup provably reduces calibration error [8]. The expected calibration error (ECE) and its variants serve as standard metrics for evaluating calibration quality [14][15]. Our proposed Smooth Calibration Loss builds upon these foundations by introducing a necessary condition for ideal calibration, aiming to achieve superior calibration performance in complex scenarios.

---

## References

[1] Verified Uncertainty Calibration. (2019). arXiv:1909.10155.

[2] Adaptive Temperature Scaling for Robust Calibration of Deep Neural Networks. (2022). arXiv:2208.00461.

[3] Calibration of Machine Learning Classifiers for Probability of Default Modelling. (2017). arXiv:1710.08901.

[4] Wehenkel, A. & Louppe, G. (2019). Unconstrained Monotonic Neural Networks. arXiv:1908.05164.

[5] Binary Classifier Calibration using an Ensemble of Near Isotonic Regression Models. (2015). arXiv:1511.05191.

[6] Classifier Calibration with ROC-Regularized Isotonic Regression. (2023). arXiv:2311.12436.

[7] Zhang, H. et al. (2017). mixup: Beyond Empirical Risk Minimization. arXiv:1710.09412.

[8] When and How Mixup Improves Calibration. (2021). arXiv:2102.06289.

[9] RankMixup: Ranking-Based Mixup Training for Network Calibration. (2023). arXiv:2308.11990.

[10] Neural Clamping: Joint Input Perturbation and Temperature Scaling for Neural Network Calibration. (2022). arXiv:2209.11604.

[11] Adaptive Temperature Scaling for Robust Calibration of Deep Neural Networks. (2022). arXiv:2208.00461.

[12] Wehenkel, A. & Louppe, G. (2019). Unconstrained Monotonic Neural Networks. arXiv:1908.05164.

[13] SortNet: Learning To Rank by a Neural-Based Sorting Algorithm. (2023). arXiv:2311.01864.

[14] Estimating Expected Calibration Errors. (2021). arXiv:2109.03480.

[15] Smooth ECE: Principled Reliability Diagrams via Kernel Smoothing. (2023). arXiv:2309.12236.
