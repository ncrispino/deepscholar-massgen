# Related Works

The evaluation of fairness in machine learning systems has gained significant attention as large language models (LLMs) become increasingly integrated into high-stakes decision-making applications. This section reviews prior work across four key dimensions: traditional fairness metrics, bias in NLP systems, uncertainty quantification in deep learning, and existing LLM benchmarks.

## Traditional Fairness Metrics

Conventional fairness definitions in machine learning primarily focus on demographic parity and equalized odds [1]. Hardt et al. [1] formalized Equalized Odds as a criterion requiring that prediction outcomes be independent of protected attributes conditional on the true label. While foundational, these metrics evaluate fairness based solely on discrete prediction correctness, overlooking the model's confidence and uncertainty in its outputs. Subsequent work has explored additional fairness criteria including calibration and individual fairness [2], though these approaches similarly treat model outputs as deterministic.

## Gender and Occupational Bias in NLP

A substantial body of research has documented gender and occupational bias in language models and NLP systems. Bolukbasi et al. [3] demonstrated that word embeddings encode and amplify gender stereotypes, particularly in occupation-gender associations. Rudinger et al. [4] extended this analysis to neural coreference resolution systems, showing systematic failures in pronoun resolution based on gender. Zhao et al. [5] identified gender bias amplification in vision-and-language datasets, where models inherit and magnify societal stereotypes. These findings highlight the persistent challenge of measuring and mitigating bias across different NLP tasks and data modalities.

## Uncertainty Quantification in Deep Learning

Recent advances in uncertainty quantification provide tools for understanding model confidence beyond point predictions. Kendall and Gal [6] distinguished between epistemic uncertainty (model uncertainty reducible through additional data) and aleatoric uncertainty (irreducible data noise), demonstrating their importance for reliable deep learning. Dropout-based Bayesian approximations [7] and ensemble methods have emerged as practical approaches for estimating prediction uncertainty. However, the application of these uncertainty measures to fairness evaluation remains underexplored.

## LLM Benchmarks and Evaluation

Multiple benchmarks have been proposed to assess LLM capabilities and limitations. Bilingual Evaluation Understudy (BLEU) [8] and Recall-Oriented Understudy for Gisting Evaluation (ROUGE) [9] metrics provided early foundations for language generation evaluation. More recent work has examined specific dimensions of LLM trustworthiness [10], though comprehensive fairness evaluation with uncertainty awareness remains limited. The evaluation datasets proposed in prior work often suffer from limited size, demographic homogeneity, or ambiguities that complicate precise fairness assessment [4][5].

## Contributions of This Work

This paper extends prior work by introducing an uncertainty-aware fairness metric (UCerF) that captures implicit biases in model confidence across demographic groups. Unlike traditional fairness measures [1], our approach provides fine-grained evaluation of model fairness by incorporating uncertainty into the fairness assessment. Additionally, we contribute a comprehensive gender-occupation fairness dataset with 31,756 samples specifically designed for coreference resolution, addressing the dataset limitations identified in prior work.

---

## References

[1] Hardt, M., Price, E., & Srebro, N. (2016). Equality of Opportunity in Supervised Learning. arXiv:1611.01567.

[2] Dwork, C., Hardt, M., Pitassi, T., Reingold, O., & Zemel, R. (2012). Fairness Through Awareness. arXiv:1104.3913.

[3] Bolukbasi, T., Chang, K. W., Zou, J., Saligrama, V., & Kalai, A. (2016). Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings. arXiv:1607.06520.

[4] Rudinger, R., Naradowsky, J., Leonard, B., & Van Durme, B. (2018). Gender Bias in Neural Coreference Resolution. arXiv:1804.06752.

[5] Zhao, J., Wang, T., Yatskar, M., Ordonez, V., & Chang, K. W. (2017). Men Also Like Shopping: Reducing Gender Bias Amplification using Corpus-level Constraints. arXiv:1707.09457.

[6] Kendall, A., & Gal, Y. (2017). What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision? arXiv:1703.04977.

[7] Gal, Y., & Ghahramani, Z. (2016). Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning. arXiv:1506.02142.

[8] Papineni, K., Roukos, S., Ward, T., & Zhu, W. J. (2002). BLEU: A Method for Automatic Evaluation of Machine Translation. arXiv:0209116.

[9] Lin, C. Y. (2004). ROUGE: A Package for Automatic Evaluation of Summaries. arXiv:0409059.

[10] Wang, B., Zheng, N., Chen, J., & Zhou, S. (2023). DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models. arXiv:2306.11698.