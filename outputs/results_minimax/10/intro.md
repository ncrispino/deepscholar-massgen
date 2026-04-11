# Related Works

Multi-token prediction (MTP) has emerged as a promising alternative to the standard next-token prediction (NTP) objective for language model pre-training [1][2]. Rather than predicting a single token at each step, MTP employs multiple prediction heads to forecast the next k tokens simultaneously [1]. This approach has demonstrated improved downstream performance and inference speed, particularly for large models [1][2]. Gloeckle et al. [1] showed that MTP enables better sample efficiency during training and facilitates self-speculative decoding at inference time, where the model verifies its own predictions in parallel rather than relying on a separate draft model.

Self-speculative decoding, where a language model uses its own predictions as draft tokens for verification, was introduced by Leviathan et al. [3] as "Fast Inference from Transformers via Speculative Decoding." This technique achieves sub-linear decoding latency by enabling parallel verification of multiple tokens [3]. Chen et al. [4] further developed this concept with SpecInfer, a system that combines multiple small draft models for speculative inference [4]. The original MTP work [1] noted that self-speculative decoding provides particularly strong benefits for large models, though its applicability to smaller models remained an open question.

Curriculum learning, which trains models on progressively more complex tasks, has been extensively studied in machine learning [5][6]. Bengio et al. [5] introduced the foundational concept of curriculum learning, demonstrating that presenting training examples in a meaningful order can improve both convergence speed and final model performance. Hacohen and Weinshall [6] provided theoretical and empirical support for curriculum learning in neural networks. Within language model training, curriculum approaches have shown promise for adapting models to increasingly complex objectives [7].

Recent work has specifically examined the challenges faced by small language models (SLMs) in learning complex training objectives [8]. Méaudre et al. [8] investigated the limitations of SLMs with respect to architectural choices and training objectives, finding that techniques effective for large models often fail to transfer to smaller scales. This work motivates the need for specialized training strategies, such as curriculum approaches, to help SLMs benefit from advanced objectives like MTP.

The proposed curriculum learning strategy for MTP training directly addresses the gap between the demonstrated benefits of MTP for large models and the challenges SLMs face in learning this objective. By gradually transitioning from NTP to MTP (forward curriculum) or in reverse (reverse curriculum), our approach enables SLMs to better leverage multi-token prediction while retaining the inference benefits of self-speculative decoding.

---

## References

[1] Gloeckle, F., Idrissi, B. Y., Rozière, B., Lopez-Paz, D., & Synnaeve, G. (2024). Multi-token prediction. *arXiv:2405.04330*.

[2] Sun, Z., Li, Y., Zhang, T., Zhong, L., Nguyen, D., & Liu, Y. (2024). Lorenzo: Multi-token prediction with sparse attention. *arXiv:2407.21748*.

[3] Leviathan, Y., Kalman, M., & Matias, Y. (2023). Fast inference from transformers via speculative decoding. *arXiv:2211.17192*.

[4] Chen, Z., Wu, J., Zhou, W., Li, B., Zhou, W., Lin, D., et al. (2023). SpecInfer: Accelerating large language model serving with tree-based speculative inference. *arXiv:2302.01318*.

[5] Bengio, Y., Louradour, J., Collobert, R., & Weston, J. (2009). Curriculum learning. *Proceedings of the 26th Annual International Conference on Machine Learning*, 41-48.

[6] Hacohen, G., & Weinshall, D. (2019). On the power of curriculum learning in training deep networks. *Proceedings of the 36th International Conference on Machine Learning*, 2535-2544.

[7] Popel, M., & Bojar, O. (2018). Training tips for the transformer model. *arXiv:1804.00247*.

[8] Méaudre, G., Ligozat, A.-L., & François, O. (2024). Small language models: Lessons from the LLM revolution and future directions. *arXiv:2404.12008*.