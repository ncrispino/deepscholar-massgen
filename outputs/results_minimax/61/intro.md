# Related Works

This section reviews prior research in three key areas relevant to FashionDPO: fashion outfit generation and compatibility learning, personalized fashion recommendation, and preference optimization in generative models.

## Fashion Outfit Generation and Compatibility

Fashion outfit generation requires both aesthetic judgment and an understanding of item compatibility. Early approaches to outfit composition treat it as a recommendation problem, generating items that complement a partial outfit or suggesting complete outfits from scratch [1][2]. Chen et al. [3] conducted experimental studies demonstrating that successful outfit generation depends on balancing item-level quality with ensemble-level coherence.

Graph-based methods have become dominant for modeling outfit compatibility. These approaches represent fashion items as nodes and compatibility relationships as edges, enabling message passing through graph neural networks (GNNs) to learn latent compatibility patterns [4][5]. Song et al. [6] proposed transformer-based GNN architectures specifically designed for outfit generation, capturing both local item features and global outfit structure. Research has also explored specific compatibility dimensions, including style matching [7] and color harmony [8], which provide interpretable signals for compatibility assessment.

## Personalized Fashion Recommendation

Personalization in fashion recommendation addresses the challenge of aligning outfit suggestions with individual user preferences. Traditional methods rely on collaborative filtering to leverage preference patterns across users [9]. More recent approaches incorporate visual features directly, enabling systems to understand style preferences from user interaction histories [10]. Contrastive learning frameworks have proven effective for learning discriminative user representations in the fashion domain [11], addressing cold-start problems by learning transferable preference embeddings.

## Generative Models and Preference Optimization

Recent advances in diffusion models have enabled high-quality fashion item synthesis [7], but these generative approaches face challenges in aligning outputs with user preferences without extensive labeled data. Direct Preference Optimization (DPO) and its variants provide a promising direction by fine-tuning models using preference feedback rather than explicit reward functions. RS-DPO [12] combines rejection sampling with DPO to improve alignment quality, while Step-DPO [13] extends the approach to multi-step reasoning tasks.

Despite progress in both fashion recommendation and preference optimization independently, there remains a gap in applying preference-based fine-tuning to fashion outfit generation. Existing methods either lack the ability to generate novel outfits or require task-specific reward engineering. FashionDPO bridges this gap by introducing a multi-expert feedback mechanism that evaluates generated outfits across quality, compatibility, and personalization dimensions, enabling general fine-tuning of fashion generative models without task-specific reward design.

---

## References

[1] POG: Personalized Outfit Generation for Fashion. arXiv:1905.01866.

[2] Mining Fashion Outfit Composition. arXiv:1608.03016.

[3] Outfit Generation and Recommendation: An Experimental Study. arXiv:2211.16353.

[4] Reusable Self-Attention-based Recommender System for Fashion. arXiv:2211.16366.

[5] Hierarchical Fashion Graph Network for Outfit Recommendation. arXiv:2005.12566.

[6] Transformer-based Graph Neural Networks for Outfit Generation. arXiv:2304.08098.

[7] Diffusion Models for Generative Outfit Recommendation. arXiv:2402.17279.

[8] Fashion Recommendation: Outfit Compatibility using Graph Neural Networks. arXiv:2404.18040.

[9] Recommendation of Compatible Outfits Conditioned on Style. arXiv:2203.16161.

[10] Learning Color Compatibility in Fashion Outfits. arXiv:2007.02388.

[11] Contrastive Learning for Interactive Recommendation in Fashion. arXiv:2207.12033.

[12] RS-DPO: Hybrid Rejection Sampling and Direct Preference Optimization. arXiv:2402.10038.

[13] Step-DPO: Step-wise Preference Optimization for LLM. arXiv:2406.18629.
