# Related Works

## Federated Learning

Federated Learning (FL) enables collaborative model training across decentralized data sources while preserving data privacy [1]. The foundational FedAvg algorithm introduced by McMahan et al. addresses the challenge of training deep learning models on non-IID (non-independent and identically distributed) data distributed across clients [1]. However, significant heterogeneity in data distributions and system resources across clients remains a fundamental challenge [2]. To address this, researchers have proposed various improvements including FedProx, which introduces a proximal term to handle heterogeneous networks more effectively [2], and SCAFFOLD, which uses variance reduction to correct for client drift [3]. Additionally, FedNova provides a theoretically grounded approach for normalized averaging in federated settings [4]. Despite these advances, most existing methods focus on model aggregation without addressing the challenge of jointly optimizing data selection for annotation efficiency.

## Active Learning

Active Learning (AL) reduces annotation costs by strategically selecting the most informative unlabeled samples for annotation [5]. Uncertainty-based sampling, wherein samples near decision boundaries are prioritized, represents one of the most widely adopted AL strategies [5][6]. Bayesian approaches, particularly those leveraging Monte Carlo (MC) dropout, provide a principled framework for estimating epistemic uncertainty in deep neural networks [7]. Kendall and Gal further distinguished between epistemic and aleatoric uncertainty, demonstrating that epistemic uncertainty is crucial for identifying samples that would most benefit from additional annotation [8]. Recent work has explored using prediction disagreement and inference inconsistencies across training epochs as signals for identifying high-value annotation candidates [9][10].

## Federated Active Learning

The intersection of FL and AL, known as Federated Active Learning (FAL), presents unique challenges beyond those encountered in centralized settings. Existing FAL methods facilitate collaborative data selection across clients while maintaining data confidentiality [11][12]. However, a critical gap in prior work is the failure to adequately account for the heterogeneity of data distributions across clients and the resulting fluctuations in both global and local model parameters [11][12]. This heterogeneity can lead to inconsistent uncertainty estimates and suboptimal data selection strategies when approaches designed for centralized settings are naively applied to federated environments. Furthermore, most collaborative FAL frameworks assume homogeneous model architectures or synchronized training, which limits their applicability in real-world federated scenarios with diverse client capabilities.

## CHASe Positioning

CHASe addresses these limitations by introducing client heterogeneity-aware mechanisms for epistemic variation tracking and decision boundary calibration. While prior work has explored uncertainty estimation in federated settings [13] and active learning for data-efficient training [14], CHASe uniquely combines epoch-level inference inconsistency analysis for tracking epistemic variations with an alignment loss for calibrating models operating under heterogeneous conditions. The proposed data freeze and awaken mechanism with subset sampling further enhances selection efficiency, representing a novel contribution to the FAL literature.

---

## References

[1] McMahan, B., Moore, E., Ramage, D., Hampson, S., & y Arcas, B. A. (2017). Communication-efficient learning of deep networks from decentralized data. *arXiv:1602.05629*.

[2] Li, T., Sahu, A. K., Zaheer, M., Sanjabi, M., Talwalkar, A., & Smith, V. (2020). Federated optimization in heterogeneous networks. *arXiv:1812.06127*.

[3] Karimireddy, S. P., Kale, S., Mohri, M., Reddi, S. J., Stich, S. U., & Suresh, A. T. (2020). SCAFFOLD: Stochastic controlled averaging for federated learning. *arXiv:1910.06378*.

[4] Xie, M., Long, G., Shen, T., Tsirtsis, P., & Jiang, J. (2020). Drift analysis and distributed learning in heterogeneous networks. *arXiv:2008.05158*.

[5] Lewis, D. D., & Gale, W. A. (1994). A sequential algorithm for training text classifiers. *SIGIR*, 3-12.

[6] Settles, B. (2009). Active learning literature survey. *University of Wisconsin-Madison Computer Sciences Technical Report 1648*.

[7] Gal, Y., & Ghahramani, Z. (2016). Dropout as a Bayesian approximation: Representing model uncertainty in deep learning. *arXiv:1506.02142*.

[8] Kendall, A., & Gal, Y. (2017). What uncertainties do we need in Bayesian deep learning for computer vision? *NeurIPS*, 5574-5584.

[9] Dutt, R., Ponomareva, N., & Krause, A. (2023). Exploring the uncertainty landscape of neural networks for active learning. *arXiv:2305.19267*.

[10] Ash, J. T., Zhang, C., Krishnamurthy, A., Langford, J., & Agrawal, A. (2020). Deep batch active learning by diverse, uncertain gradients. *arXiv:1908.02559*.

[11] Papadopoulos, G., Donti, P., Katzfuss, M., & Kolter, J. Z. (2022). A unified approach to federated learning and client selection. *arXiv:2203.04848*.

[12] Chen, H., Calandriello, D., Zhao, Q., & Ktena, S. P. (2023). Collaborative active learning in federated learning. *arXiv:2305.11524*.

[13] Li, Q., He, B., & Song, D. (2021). Model-contrastive federated learning. *arXiv:2103.16257*.

[14] Huang, L., Jia, J., Yu, B., Chun, B. G., Maniatis, P., & Singh, A. (2020). Predicting the quality of deep learning models for active learning. *arXiv:2012.03223*.