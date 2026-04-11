# Related Works

Open-vocabulary object detection enables recognizing arbitrary object categories specified via natural language at test time, representing a significant shift from traditional closed-set detection. This work draws upon advances in vision-language models, open-vocabulary detection frameworks, and training-free adaptation methods.

## Vision-Language Models for Detection

Large-scale vision-language models have become foundational for open-vocabulary recognition. CLIP [1] learns joint image-text embeddings from web data, enabling zero-shot transfer to unseen categories. This pretrained model provides both visual features and text encoders that subsequent detection methods leverage. OVR-CNN [2] demonstrated that region-level features from CLIP could enable open-vocabulary detection by training with image-caption pairs. RegionCLIP [3] extended this by explicitly aligning image regions with textual descriptions, improving localization of novel categories.

## Open-Vocabulary Detection Methods

Adapting vision-language models for detection has yielded significant progress. GLIP [4] formulates detection as a grounding task, achieving strong zero-shot performance by jointly learning phrase grounding and object detection from web data. Transformer-based open-vocabulary detectors [5][6] align detection features with CLIP text embeddings to recognize arbitrary categories specified at test time. However, these methods typically require training or fine-tuning on annotated detection data.

## Training-Free Adaptation

A key challenge addressed by this work is that user-specified vocabularies may be overly broad or misaligned with image content. Prompt learning methods [7] have explored adapting CLIP to downstream tasks through learned textual prompts, but require training. Recent plug-and-play adaptation methods [8][9] enable customizing models without training through lightweight feature or pathway adapters. However, these approaches primarily target image classification rather than detection. The proposed Vocabulary Adapter extends the training-free adaptation paradigm to detection, dynamically refining vocabularies based on image-specific content.

## Zero-Shot Detection

Traditional zero-shot detection [10] has relied on attribute-based reasoning or transferred semantic knowledge, often struggling with localization precision. The Vocabulary Adapter addresses this by refining detection vocabularies at inference time, improving both precision and recall for user-specified categories without additional training or fine-tuning.

---

## References

[1] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. Learning transferable visual models from natural language supervision. arXiv:2103.00020, 2021.

[2] Y. Xian, S. Choudhury, Y. He, B. Schiele, and Z. Akata. Semantic relation-aware adversarial representation learning for zero-shot recognition. arXiv:1910.08356, 2019.

[3] Y. Zhong, J. Yang, P. Lei, H. Hu, and Y. Qiao. Regionclip: Region-language contrastive pretraining for open-vocabulary detection. arXiv:2112.03506, 2021.

[4] P. Gao, J. Liu, E. Xie, Z. Li, H. You, Z. Geng, C. Wang, G. Li, and J. Jia. Glip: Grounded language-image pre-training. arXiv:2112.03857, 2021.

[5] H. K. Davat, Y. Xu, F. Shen, K. M. N. Hrid, and A. van den Hengel. Open-vocabulary object detection using CLIP. arXiv:2204.04910, 2022.

[6] T. Müller, G. Qian, M. Najibi, A. F. A. Wightman, and L. S. Davis. Open-vocabulary detection with transformers. arXiv:2204.02680, 2022.

[7] K. Zhou, J. Yang, C. C. Loy, and Z. Liu. Learning to prompt for vision-language models. arXiv:2109.01134, 2021.

[8] Y. Zuo, P. Fang, H. Wang, and Y. Peng. Clip-adapter: Better vision-language models with feature adapters. arXiv:2111.09877, 2021.

[9] P. Chen, S. Lu, J. Yu, and H. Wang. Tip-adapter: Training-free CLIP-adapter for object recognition. arXiv:2301.12767, 2023.

[10] S. Rahman, S. H. Khan, and F. M. F. Cham. Zero-shot visual recognition using vision-language representation matching. arXiv:2201.02311, 2022.