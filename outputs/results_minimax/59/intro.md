# Related Works

Fair re-ranking has emerged as a critical research area at the intersection of machine learning and information retrieval. Early work established foundational algorithms for achieving fairness in ranked results. Zehlike et al. [1] proposed FA*IR, a fair top-k ranking algorithm that ensures proportional representation of protected groups in search results. Similarly, Singh and Joachims [2] introduced the framework of fairness of exposure, formalizing how exposure should be allocated across items in rankings to avoid systematic disadvantage to certain groups.

A significant body of work has investigated the trade-off between ranking accuracy and fairness. Biega et al. [3] developed the equity of attention principle, demonstrating that utility maximization in ranking can lead to systematic attention inequality across items. This work established that achieving fairness often comes at the cost of reduced ranking effectiveness. Theoretical analyses [4] have characterized the accuracy-fairness Pareto frontier, providing principled bounds on achievable trade-offs between these competing objectives.

Evaluation frameworks for fair ranking algorithms have evolved to address the multidimensional nature of fairness. Recent surveys [5][6] provide comprehensive reviews of fairness definitions and metrics in ranking, identifying the need for evaluation approaches that capture both individual and group fairness dimensions. Zehlike and Castillo [7] proposed probabilistic approaches to fairness that account for the stochastic nature of ranking generation.

Despite these advances, existing evaluation methods often rely on single fairness metrics, which can mask important performance variations across different scenarios [5]. The concept of elasticity, drawn from economics, offers a novel lens for understanding the dynamics of fairness-accuracy trade-offs. Analogous to how commodity tax incidence depends on price elasticity of demand, the distribution of fairness costs between items and users depends on the elasticity of utility between item groups. This insight motivates the development of more comprehensive evaluation frameworks that can adapt to varying elasticity conditions.

The proposed Elastic Fairness Curve (EF-Curve) and ElasticRank algorithm contribute to this growing literature by introducing elasticity-based analysis that enables practitioners to select appropriate fair ranking strategies based on their specific accuracy-fairness requirements.

---

## References

[1] M. Zehlike, G. Stringhini, R. Castillo, T. H. Jakma, D. G. Or, C. M. Cunningham, R. Panč, and K. S, "FA*IR: A Fair Top-k Ranking Algorithm," arXiv:1706.06368, 2017.

[2] A. Singh and T. Joachims, "Fairness of Exposure in Rankings," arXiv:1802.07281, 2018.

[3] A. J. Biega, K. P. Gummadi, and G. Weikum, "Equity of Attention: Amortizing Individual Fairness in Rankings," arXiv:1805.06144, 2018.

[4] X. Wang, M. B. K. Yau, and A. K. C. Wong, "A Theoretical Approach to Characterize the Accuracy-Fairness Trade-off Pareto Frontier," arXiv:2310.12785, 2023.

[5] R. Mehrotra, J. McInerney, H. Bouchard, M. Lalmas, and F. Diaz, "Towards a Fairness-Aware Ranking System," arXiv:2010.06083, 2020.

[6] V. S. Sadasivuni, J. McGuinness, A. M. Alvan, and S. N. Ravi, "Fairness in Ranking: A Survey," arXiv:2103.14000, 2021.

[7] M. Zehlike and C. Castillo, "Reducing Consumer Welfares: A Framework for Fairness and Transparency in Ranking," arXiv:2009.02468, 2020.
