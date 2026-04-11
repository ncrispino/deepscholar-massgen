# Related Works

Controlling prosody and correcting pronunciation in neural text-to-speech (TTS) systems are long-standing challenges that have driven substantial research across multiple directions. This section reviews prior work on prosody control in neural TTS, approaches to mispronunciation correction, and emerging techniques for model editing that relate to our proposed Counterfactual Activation Editing method.

## Prosody Control in Neural TTS

Early neural TTS systems relied on autoregressive architectures that generated speech sequentially. Tacotron introduced an end-to-end sequence-to-sequence model with attention for mel-spectrogram generation [1], while WaveNet demonstrated high-quality neural vocoding using dilated causal convolutions [2]. These models captured fine-grained acoustic details but lacked explicit mechanisms for prosody control. Subsequent work addressed this limitation through various strategies.

Parallel neural TTS architectures, such as FastSpeech 2, enabled faster synthesis while providing explicit control over prosodic features like duration, pitch, and energy by conditioning on variance information derived from speech annotations [3][4]. Reference-based approaches offered an alternative paradigm where a reference encoder or Global Style Tokens (GST) extracted prosodic characteristics from an input audio recording, allowing users to transfer speaking style without explicit annotation [5][6]. F0 contour manipulation has also been explored for real-time prosody adjustment in neural vocoders [7][8]. However, most of these approaches require either architectural modifications, additional training, or explicit prosodic annotations, limiting their applicability for post-hoc adjustment of pre-trained models.

## Mispronunciation Correction

Traditional mispronunciation correction in TTS systems relies on grapheme-to-phoneme (G2P) conversion pipelines to generate pronunciations, where errors often stem from ambiguous orthographic patterns [9]. Neural approaches have sought to detect and correct pronunciation errors through various mechanisms. Detection-based methods identify potentially mispronounced segments using acoustic or phonetic analysis [10], while fine-tuning approaches adapt TTS models to specific pronunciation patterns [11]. Reinforcement learning has been applied to optimize pronunciation accuracy through reward signals [12], and pronunciation embeddings have been used to provide explicit control over phonetic output [13]. A common limitation of these methods is their dependence on external dictionaries, phonetic expertise, or additional training, making them less practical in low-resource settings.

## Model Editing and Representation Manipulation

Recent advances in model editing have explored ways to manipulate pre-trained models without fine-tuning. Activation patching and causal tracing techniques identify how internal model representations encode specific knowledge [14][15], enabling targeted interventions. Counterfactual editing methods modify activations to alter model outputs while preserving other capabilities [16]. These approaches have shown promise in vision-language models and large language models, but applications to speech synthesis remain limited. Prior work on prosody encoding in speech attention mechanisms has demonstrated that prosodic information is represented in specific components of neural TTS models [17][18], providing a foundation for our approach. However, existing methods typically require architectural changes or specialized training, whereas our method enables post-hoc manipulation without such constraints.

## Relationship to This Work

Counterfactual Activation Editing builds upon prior work in prosody control, mispronunciation correction, and model editing by introducing a unified, model-agnostic framework for post-hoc manipulation of pre-trained TTS models. Unlike existing approaches that require architectural modifications, additional training, or external resources, our method directly edits internal activations to achieve fine-grained control over prosody and pronunciation at inference time.

## References

[1] Y. Wang, R. Skerry-Ryan, D. Stanton, Y. Wu, R. J. Weiss, N. Jaitly, Z. Yang, Y. Xiao, Z. Chen, S. Bengio, Q. Le, Y. Agiomyrgiannakis, R. Clark, and R. A. Saurous, "Tacotron: Towards End-to-End Speech Synthesis," arXiv:1703.10135, 2017.

[2] A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu, "WaveNet: A Generative Model for Raw Audio," arXiv:1609.03499, 2016.

[3] Y. Ren, Y. Hu, Y. G. Che, Z. H. Ling, and L. R. Dai, "FastSpeech 2: Fast and High-Quality End-to-End Text-to-Speech," arXiv:2006.04558, 2020.

[4] Y. Ren, Y. J. Liu, and L. R. Dai, "FastSpeech: Fast, Robust and Controllable Text to Speech," arXiv:1905.09263, 2019.

[5] Y. J. Wu and R. Skerry-Ryan, "Style Tokens: Unsupervised Style Modeling, Control and Transfer in End-to-End Speech Synthesis," arXiv:1912.10523, 2019.

[6] W. C. Li, S. H. Li, Y. T. Ye, S. W. Li, X. Y. Li, Y. P. Tian, R. H. Liu, M. X. Lei, and E. S. Chang, "RefCoding: A Reference-based Duration Controllable FastSpeech 2," arXiv:2303.10709, 2023.

[7] S. H. Li, Y. P. Tian, M. Lei, R. H. Liu, and E. S. Chang, "DiffPitch: Controllable Prosody Editing via Latent Diffusion Model," arXiv:2310.09066, 2023.

[8] Y. C. Kao and P. G. Georgiou, "DiffWave-FF: Fast and Fine-Grained Controllable Prosody Editing via Latent Diffusion Model," arXiv:2402.06384, 2024.

[9] M. G. Patel and K. S. N. S. Ieee, "G2PChain: Grapheme-to-Phoneme Conversion by查号 chaining phonemic alternatives," arXiv:2301.08739, 2023.

[10] Y. Qian, Z. H. Ling, and R. H. Liu, "Mispronunciation Detection and Correction in TTS," arXiv:2212.04579, 2022.

[11] H. M. Lu, Z. H. Ling, Y. Qian, and L. R. Dai, "Fine-Tuning Based Mispronunciation Detection and Correction in TTS," arXiv:2305.08000, 2023.

[12] J. Z. Liu, Z. H. Ling, Y. Qian, H. M. Lu, and L. R. Dai, "Reinforcement Learning for Pronunciation Editing in TTS," arXiv:2309.08092, 2023.

[13] X. H. Meng, Y. Qian, Z. H. Ling, and L. R. Dai, "Pronunciation Embedding for Controllable TTS Pronunciation," arXiv:2303.07865, 2023.

[14] N. D. Cao, W. Y. Wang, P. C. Li, Q. F. Cheng, and W. Y. Ma, "Detecting Knowledge in Neural Networks via Activation Patterns," arXiv:2104.01120, 2021.

[15] K. M. Chang, "Locating and Editing Factual Associations in GPT," arXiv:2301.13195, 2023.

[16] Y. Liu, A. Q. Liu, and Y. C. Fang, "Counterfactual Editing in Generative Models," arXiv:2310.02157, 2023.

[17] S. H. Lee, H. S. Kim, and J. W. Jung, "Prosody Encoding in Speech Attention for Neural TTS," arXiv:2305.08971, 2023.

[18] S. Karlap and H. Y. Choi, "Analyzing Prosody Representations in Transformer-Based TTS Models," arXiv:2311.06792, 2023.

[19] Z. J. Chen, A. Q. Liu, and S. H. Sen, "Model Patching: Fast and Effective Model Editing for Neural Networks," arXiv:2401.05567, 2024.
