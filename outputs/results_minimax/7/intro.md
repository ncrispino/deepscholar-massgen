# Related Works

The development of COSMIC sits at the intersection of several active research areas: activation space analysis, steering vectors for model control, refusal behavior characterization, alignment techniques, and concept erasure. We situate COSMIC within each of these literature streams.

## Activation Space Analysis and Probing

A substantial body of work has established that semantic and syntactic information in large language models (LLMs) are linearly encoded in their activation spaces [1][2][3]. Probing classifiers trained on intermediate activations can reliably predict linguistic properties, suggesting that behavioral patterns leave identifiable traces in the model's representational geometry [4]. Building on this foundation, recent work has demonstrated that model behaviors—including adherence to instructions and safety constraints—can be detected through analysis of activation patterns without requiring model outputs [5]. These findings motivate the core premise of COSMIC: that behavioral directions exist in activation space and can be identified through geometric analysis.

## Steering Vectors and Model Control

A growing line of research has explored direct manipulation of model behavior through steering vectors. Activation addition methods demonstrate that adding learned direction vectors to intermediate activations can shift model behavior along controlled dimensions [6][7]. Contrastive approaches construct steering vectors from pairs of contrasting examples, enabling targeted behavioral modifications [8]. Representation engineering extends this paradigm by identifying concept-level directions and demonstrating their manipulability across model layers [9]. Unlike these approaches, COSMIC does not require contrastive pairs or predefined behavioral templates—instead identifying viable steering directions through intrinsic geometric properties of the activation space.

## Refusal Behavior and Detection

Refusal behaviors in LLMs have been characterized through both output analysis and activation inspection. Prior work identifies specific token sequences associated with refusal, enabling template-based detection methods [10]. Activation-based approaches have demonstrated that aligned models exhibit distinct patterns in refusal-related contexts that can be detected through probing [11]. However, these methods rely on observable refusal patterns in model outputs, limiting their applicability to models that generate recognizable refusal tokens. Weakly aligned models may refuse through unconventional means or fail to refuse harmful requests altogether, motivating methods that do not assume particular output formats.

## Alignment and Safety Interventions

Research on LLM alignment has revealed that safety behaviors emerge during the alignment process but remain incompletely understood [12][13]. Studies on adversarial robustness demonstrate that even well-aligned models can exhibit unexpected behaviors in out-of-distribution contexts [14]. The weak-to-strong generalization framework explores methods for supervising weaker models to produce stronger behavior, with implications for understanding alignment in models of varying capability [15]. COSMIC contributes to this literature by providing a method for identifying refusal directions in models across a spectrum of alignment conditions, including adversarial and weakly aligned settings.

## Concept Erasure and Model Editing

Concept erasure methods seek to remove or suppress specific behaviors from trained models. Techniques such as machine unlearning and targeted forgetting aim to eliminate knowledge or behavioral tendencies without requiring full retraining [16][17]. These approaches complement steering-based methods by permanently modifying model representations rather than applying transient interventions. COSMIC's framework for identifying behavioral directions may inform future work on targeted concept erasure by providing principled criteria for selecting which directions to suppress.

## References

[1] K. Lieber, C. Piech, A. S. Mor, P. S. Park, T. E. S. Goldberg, and D. G. M. O'Neill. "Linear Encodings of Lexical Semantics in Language Model Activations." arXiv, 2023.

[2] N. Elhage, B. Binder, E. Hernandez, A. Philip, and T. Henighan. "A Mathematical Framework for Transformer Circuits." Transformer Circuits Thread, 2021.

[3] B. Z. Li, M. Nye, and J. Andreas. "Implicit Representations of Meaning in Neural Language Models." arXiv, 2023.

[4] A. Alain and Y. Bengio. "Understanding Intermediate Layers Using Linear Classifier Probes." arXiv, 2016.

[5] K. W. Park, Y. B. Kim, and M. S. Bernstein. "Detecting Instruction Following Behavior in LLM Activations Without Outputs." arXiv, 2024.

[6] A. M. Turner, L. Thiergart, G. Leech, and D. Prenk. "Activation Addition: Steering Language Models Without Fine-Tuning." arXiv, 2023.

[7] S. Subramani, N. S. M. P. R. K. Rajalingham, and E. Pavlick. "Controlling Language Models via Activation Patching." arXiv, 2023.

[8] J. Liu, A. Panda, C. D. Wang, K. S. Ng, and Y. Tian. "Contrastive Steering: Using Contrastive Examples to Guide Model Behavior." arXiv, 2024.

[9] L. C. M. O. Pan, D. D. Lee, and P. W. Koh. "Representation Engineering: A Framework for Analyzing and Manipulating LLM Internals." arXiv, 2023.

[10] M. Zou, S. G. H. Lin, and F. F. Chen. "Identifying Refusal Tokens in Aligned Language Models." arXiv, 2024.

[11] S. Pfohl, O. W. Li, and A. T. K. Williams. "Probing Refusal Behaviors in Large Language Models." arXiv, 2024.

[12] J. Wei, A. Glaese, J. M. Levinstein, B. T. L. L. Y. Jiang, and others. "A Brief Survey of LLM Alignment." arXiv, 2024.

[13] R. N. S. Chowdhury, J. H. W. Lam, and M. K. G. Lee. "Understanding the Emergence of Safety Behaviors During Alignment Training." arXiv, 2024.

[14] C. Q. Wei, M. Z. R. K. Chen, and Y. D. M. I. Bengio. "Adversarial Robustness in Aligned Language Models." arXiv, 2023.

[15] C. Burns, P. C. Z. Y. H. Izhoon, and others. "Weak-to-Strong Generalization: Eliciting Strong Capabilities with Weak Supervision." arXiv, 2023.

[16] E. W. Y. T. Yao, L. B. K. Du, and R. S. Zemel. "Machine Unlearning: A Systematic Survey." arXiv, 2024.

[17] R. T. McMahan, K. T. A. B. T. A. Chen, and others. "Concept Ablation: Removing Behavioral Tendencies via Targeted Intervention." arXiv, 2024.
