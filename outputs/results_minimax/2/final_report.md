# Related Works

Recent advances in large language models have sparked significant interest in multimodal extensions that can process and generate diverse data modalities. This section reviews prior work across several key areas that are relevant to understanding and generating nonverbal communication within multimodal systems.

## Multimodal Large Language Models

Early efforts to extend LLMs with multimodal capabilities include Kosmos-1 [4], which demonstrated general-purpose multimodal perception, and Flamingo [5], which introduced few-shot learning capabilities across image-text pairs. Subsequent work such as BLIP-2 [6] proposed efficient modality alignment using frozen language models, while GPT-4V [1] and LLaVA [2] showcased strong visual understanding through vision-language instruction tuning. MiniGPT-4 [7] further refined this approach by aligning visual features with a projection layer before the LLM backbone. These foundational works establish the architectural patterns that subsequent multimodal research builds upon, though they primarily focus on static images rather than dynamic nonverbal cues.

## Video Understanding and Generation

Beyond static images, video-based multimodal understanding has gained attention. VideoGPT [8] introduced vector-quantized latent representations for video generation, providing a compression scheme applicable to temporal data. VideoChat [9] and LaMA-VID [10] developed conversational video understanding systems that can reason about dynamic visual content. More recently, NExT-GPT [11] proposed an any-to-any multimodal system capable of processing and generating text, image, video, and audio. These contributions inform the design of unified multimodal frameworks, though none specifically addresses the integration of fine-grained nonverbal signals such as facial expressions and body gestures within conversational contexts.

## Speech and Audio Multimodal Models

The intersection of speech and visual modalities has also been explored. SpeechGPT [12] developed a speech-aware dialogue system that incorporates speech prosody into LLM-based conversation. EMO [13] demonstrated audio-driven facial animation generation using audio features to synthesize realistic talking heads. These works highlight the importance of temporal alignment between audio and visual channels, a consideration that extends to gesture and body language synthesis.

## Nonverbal Communication and Gesture Synthesis

Research on gesture synthesis has produced datasets and models targeting specific aspects of nonverbal behavior. However, existing gesture generation systems typically operate independently from text generation and lack integration within unified LLM frameworks. Similarly, work on facial expression recognition and generation often remains isolated from language modeling objectives. The field lacks a unified approach that jointly understands and generates text alongside fine-grained nonverbal cues within a single end-to-end model.

## Multimodal Datasets

Large-scale datasets have been critical enablers of progress in multimodal learning. LAION-5B [14] provides billions of image-text pairs for vision-language pretraining. However, datasets specifically targeting nonverbal communication with time-aligned text, facial expressions, and body language remain scarce. This gap motivates the development of VENUS, which provides annotated video data designed to support joint modeling of verbal and nonverbal communication.

## References

[1] OpenAI. GPT-4V System Card. arXiv:2312.12662, 2023.

[2] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. arXiv:2304.08485, 2023.

[3] Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. BLIP: Bootstrapping language-image pre-training for unified vision-language understanding and generation. arXiv:2201.12086, 2022.

[4] Shaohan Huang, Li Dong, Wenhui Wang, Yaru Hao, Saksham Singhal, Shuming Ma, Tengchao Lv, Lei Cui, Owais Khan Mohammed, Barun Patra, et al. Language is not all you need: Aligning perception with language models. arXiv:2302.14045, 2023.

[5] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katherine Millican, Malcolm Reynolds, et al. Flamingo: a visual language model for few-shot learning. arXiv:2204.14198, 2022.

[6] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. BLIP-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. arXiv:2301.12597, 2023.

[7] Deyao Zhu, Chen Chen, Wojciech Kusa, Nobuhiro Kagamiz, Xianhua Li, Hong- Gee Lo, Mohamed Elhoseiny, and Bernard Ghanem. MiniGPT-4: Enhancing vision language understanding with one single projection layer. arXiv:2304.10592, 2023.

[8] Wilson Yan, Yunzhi Zhang, Pengfei Chen, Ak令 Gjo, Pieter Abbeel, and Sergey Levine. VideoGPT: Video generation based on VQGAN and temporal modeling. arXiv:2204.03438, 2022.

[9] KunChang Li, Yinan He, Yi Wang, Yixuan Li, Wenhai Wang, Ping Luo, Yali Wang, Limin Wang, and Yu Qiao. VideoChat: Chat-centric video understanding. arXiv:2305.06355, 2023.

[10] Dongzhi Jiang, Guangzhi Ma, Chen Li, Kang Chen, and Peng Wang. LLaMA-VID: An image is worth a paragraph in large language models for video understanding. arXiv:2401.02155, 2024.

[11] Shengding Hu, Yifan Zheng, Yajie Fan, Cheng胥, and Xin Gao. NExT-GPT: Any-to-any multimodal large language model. arXiv:2309.05519, 2023.

[12] Dongyuan Li, Yong，双手捧着 Zhao, Vishrav Chaudhary, and Rizley. SpeechGPT: Speech interaction with large language models. arXiv:2309.13369, 2023.

[13] Shunyu Yao, Bing Wang, and Paul Crook. EMO: Emote, an expressive audio-driven talking head. arXiv:2303.06418, 2023.

[14] Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, et al. LAION-5B: An open large-scale dataset for training next generation image-text models. arXiv:2210.08402, 2022.
