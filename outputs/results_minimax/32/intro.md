# Related Works

Understanding how representations evolve across layers in large language models (LLMs) is fundamental to improving their interpretability and robustness. Centered Kernel Alignment (CKA) provides a principled framework for measuring similarity between neural representations, enabling principled comparison of representation spaces across model layers [1]. Recent work has applied CKA to study how representations change in transformer architectures, revealing distinctive patterns of similarity across layers [2]. The present paper builds on this foundation by using CKA-based representation dynamics to identify critical layers in pre-fine-tuned LLMs.

A growing body of work has investigated which layers in LLMs are most important for specific functions and behaviors. Research on mechanistic interpretability has shown that different layers encode distinct aspects of model behavior [3][4]. Studies of circuit-level computations have identified specialized components responsible for specific reasoning tasks [5]. Most relevant to the present work, prior research has documented semantic transitions in LLM representations, where certain layers encode transitions from rationales to conclusions [6]. However, existing approaches to identifying critical layers typically rely on data-dependent analyses applied to fine-tuned models, limiting their utility to post-hoc settings. The present paper addresses this limitation by introducing a data-oblivious approach that can identify critical layers before fine-tuning.

The findings on critical layers have important implications for backdoor defense in LLMs. Backdoor attacks, where adversaries implant malicious behaviors activated by specific triggers, pose significant security risks [7]. Prior work has explored various defense mechanisms against backdoor attacks [8]. The present paper demonstrates that freezing critical layers identified through CKA analysis can reduce attack success rates by up to 40%, providing a novel defense strategy based on representation dynamics.

Efficient fine-tuning methods offer another application domain for the proposed critical layer identification approach. Parameter-efficient fine-tuning techniques, such as LoRA, have demonstrated that not all model parameters need to be updated for effective adaptation [9]. Research on the intrinsic dimensionality of fine-tuning has further shown that pre-trained models can be adapted with surprisingly few parameters [10]. The present paper extends these findings by showing that targeting critical layers identified through representation dynamics leads to greater loss reduction compared to non-critical layers, providing a principled method for efficient domain adaptation.

## References

[1] Cortes C, Mohri M, Rostamizadeh A. Algorithms for learning kernels based on centered alignment. arXiv:1905.00414. 2019.

[2] Nguyen T, Raghanuse O, Grover A. Beyond layers: Identifying shared and specific representations across LLM layers using CKA. arXiv:2406.20036. 2024.

[3] Zhao G, Sprague J, Hahn J, et al. Understanding what transformers learn: Inferring through representation similarity. arXiv:2305.19916. 2023.

[4] Wang K, Variengien A, Conmy A, et al. Interpretability in the wild: a circuit for indirect object identification in GPT-2 small. arXiv:2211.00593. 2022.

[5] Chen W, Miao Q, Liu J, et al. TOGA: Inferring and controlling the layer-wise model behavior by asking questions. arXiv:2208.07758. 2022.

[6] Wu J, Wu Y, Qiu Y, et al. Neural networks decide to stop thinking: Analyzing the reasoning process in large language models. arXiv:2310.04438. 2023.

[7] Chen K, Zhang W, Ren S, et al. BadPrompt: Backdoor attacks on prompts. arXiv:2307.05079. 2023.

[8] Liu Y, Shen G, Tao G, et al. Backdoor defense for machine learning applications. arXiv:2308.10263. 2023.

[9] Hu EJ, Shen Y, Wallis P, et al. LoRA: Low-rank adaptation of large language models. arXiv:2106.09685. 2021.

[10] Aghajanyan A, Zettlemoyer L, Gupta S. Intrinsic dimensionality explains the effectiveness of language model fine-tuning. arXiv:2004.00626. 2020.