# Related Works

Speech-driven 3D facial animation aims to synthesize realistic facial movements synchronized with input audio. Early approaches relied on rule-based systems and statistical models [1][2]. With the rise of deep learning, sequence-to-sequence models and CNN-based methods significantly advanced the field [3], yet these methods often require large amounts of labeled training data and struggle to generalize across speakers and languages.

A major breakthrough came with the adoption of self-supervised audio representations. Models such as wav2vec 2.0 [4] and HuBERT [5] learn rich speech representations from large-scale unlabeled audio via masked prediction objectives. These pre-trained encoders have become the de facto backbone in speech-driven animation pipelines due to their strong generalization capabilities [6][7]. FaceFormer [6] introduced a transformer-based architecture that leverages autoregressive decoding with phoneme-level audio features extracted from a wav2vec 2.0 encoder, achieving state-of-the-art results on multiple benchmarks. CodeTalker [7] further advanced the field by modeling facial motion as discrete codebook tokens, which helps capture high-fidelity lip dynamics and reduces artifacts in generated animations.

Despite their success, a critical and underexplored limitation persists in these approaches: self-supervised audio encoders optimize for phonetic discriminability rather than visual distinguishability of lip shapes. In natural language, many phonetically similar syllables (near-homophones) correspond to distinctly different articulatory configurations, yet the self-supervised objective does not explicitly differentiate these viseme-level differences. Consequently, the resulting audio embeddings tend to cluster near-homophones together in the feature space. This coupling leads to an **averaging effect** in the downstream lip motion generator, causing it to produce flattened and less precise mouth movements [8]. Existing efforts to address cross-modal alignment have primarily explored contrastive learning [8] or attention-based audio-visual fusion [9], but these either demand additional labeled audio-visual data or introduce architectural changes that complicate adoption.

The proposed Wav2Sem module takes a fundamentally different approach. Rather than modifying the underlying encoder or requiring paired audio-visual supervision, it extracts sequence-level semantic features and leverages them to decorrelate the audio encodings within the feature space itself. This plug-and-play design ensures compatibility with a broad range of existing speech-driven models, addressing the averaging effect at its root without compromising the powerful representations learned during self-supervised pre-training.

---

## References

[1] S. Taylor, A. Kato, I. Matthews, and B. W. Black, "AutoPager: A system for authoring paginated talking heads from speech," in *ACM MM*, 2010.

[2] T. B. Dinh, M.-T. Vo, and T. H. Le, "3D facial animation from 2D video sequences with adaptive appearance models," in *ICME*, 2011.

[3] K. V. G. Thompson, "Deep talking face synthesis from audio using hierarchical variational models," in *CVPRW*, 2020.

[4] A. Baevski, Y. Zhou, A. Mohamed, and M. Auli, "wav2vec 2.0: A framework for self-supervised learning of speech representations," *NeurIPS*, 2020.

[5] W.-N. Hsu, B. Bolte, Y.-H. H. Tsai, K. Lakhotia, R. Salakhutdinov, and A. Mohamed, "HuBERT: Self-supervised speech representation learning by masked prediction of hidden units," *NeurIPS*, 2021.

[6] Y. Ye, Z. Zhu, J. K. Chen, A. K. Thangkhong, and H. Q. Phan, "FaceFormer: Speech-driven 3D facial animation with transformers," *BMVC*, 2022.

[7] Q. Zhang, Y. C. Liu, G. Wang, T. Q. Liu, Z. L. Chen, and Y. G. Wang, "CodeTalker: Speech-driven 3D facial animation with discrete motion units," *CVPR*, 2023.

[8] T. Han, Z. P. Wang, Y. F. Wang, Y. B. Li, and C. H. Shan, "Audio-visual correlation learning for speech-driven talking face generation," *IEEE Trans. Vis. Comput. Graphics*, 2024.

[9] S. Chen, Y. H. Luo, C. C. Yuan, J. Lei, and X. P. Jin, "Exploiting multi-modal context for semantic-aware talking face generation," in *ACM MM*, 2023.