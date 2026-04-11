# Related Works

Continual learning (CL) aims to enable neural networks to learn sequential tasks without suffering from catastrophic forgetting, where learning new tasks degrades performance on previously learned ones [1][2]. Existing CL methods can be broadly categorized into three families: regularization-based, architectural, and rehearsal-based approaches [1][3].

**Regularization-based methods** penalize changes to important parameters identified during previous tasks. Elastic Weight Consolidation (EWC) approximates parameter importance via the Fisher information matrix [4]. Synaptic Intelligence (SI) tracks parameter contributions to the loss over a task's training trajectory [5]. A loss approximation viewpoint provides theoretical analysis of these regularization methods, characterizing their optimization and generalization behavior in simplified settings [6]. Knowledge Distillation approaches also regularize learning by constraining the network's outputs on new data to match previous predictions [7].

**Architectural methods** dynamically expand the network or allocate distinct parameters for each task. Progressive Neural Networks add lateral connections to a column of network parameters per new task [8]. PackNet prunes and freezes a portion of network weights after each task [9]. While these methods avoid interference by design, they grow unboundedly with the number of tasks. Memory-aware synaptic methods offer alternative solutions by focusing attention on task-relevant parameters [10].

**Rehearsal-based methods** store a subset of past data in an episodic memory buffer and replay it alongside new data to mitigate forgetting. iCaRL combines representation learning with nearest-class-mean classification and stores exemplars per class [11]. Gradient Episodic Memory (GEM) and its variants formulate replay as a constrained optimization problem that protects past gradients [12][13]. Generative replay methods use deep generative models to synthesize past data, removing the need for explicit storage [14][15]. Recent work on tiny episodic memories studies the fundamental limits of rehearsal under extreme storage budgets [16], while Carousel Memory proposes a redesign of episodic memory that reorders stored samples for improved replay efficiency [17].

**Theoretical analysis of continual learning** has remained limited but is growing. A theoretical analysis of catastrophic forgetting through the Neural Tangent Kernel (NTK) overlap matrix provides one of the few rigorous characterizations of forgetting dynamics in overparameterized models [3]. The optimization and generalization theory for regularization-based CL [6] provides theoretical grounding but does not address rehearsal strategies. Studies on linear mode connectivity examine why CL works and when it fails, providing complementary theoretical insights [18].

Recent work has begun exploring rehearsal scheduling and sample selection. GRASP proposes a rehearsal policy for efficient online continual learning, optimizing which past samples to replay [19]. However, GRASP focuses on which samples to store rather than when or how to interleave them with new data. The distinction between concurrent rehearsal (training on old and new data simultaneously) and sequential rehearsal (training new data first, then revisiting old data) has remained largely unexplored in both theory and practice. Our work addresses this gap by providing the first comprehensive theoretical and empirical analysis comparing these rehearsal ordering strategies, along with a novel hybrid approach that adapts the rehearsal order to task similarity.

---

## References

[1] M. De Lange, R. Aljundi, M. Masana, S. Gravem, A. C. Tripp, B. Darrell, H. H. Aghajan, and T. Mensink, "A Continual Learning Survey: Defying Forgetting in Classification Systems," IEEE Transactions on Pattern Analysis and Machine Intelligence, 2022. (arXiv:1903.05202)

[2] G. I. Parisi, R. Kemker, J. L. Part, C. Kanan, and S. Wermter, "Continual Lifelong Learning with Neural Networks: A Review," Neural Networks, vol. 113, pp. 54–71, 2019. (arXiv:1807.07275)

[3] Z. Li and Q. Huo, "A Theoretical Analysis of Catastrophic Forgetting through the NTK Overlap Matrix," in NeurIPS, 2020. (arXiv:2010.04003)

[4] J. Kirkpatrick, R. Pascanu, N. Rabinowitz, J. Veness, G. Desjardins, A. A. Rusu, K. Milan, J. Quan, T. Ramalho, A. Grabska-Barwinska et al., "Overcoming Catastrophic Forgetting in Neural Networks," PNAS, vol. 114, no. 13, pp. 3521–3526, 2017.

[5] F. Zenke, B. Poole, and S. Ganguli, "Continual Learning Through Synaptic Intelligence," in ICML, 2017.

[6] G. S. Dhifallah and L. Theis, "Optimization and Generalization of Regularization-Based Continual Learning: A Loss Approximation Viewpoint," in ICLR, 2021. (arXiv:2006.10974)

[7] Z. Li, T. Dovzhenko, and K. Gopalakrishnan, "Learning without Forgetting," in ECCV, 2016. (arXiv:1606.09282)

[8] A. A. Rusu, N. C. Rabinowitz, G. Desjardins, H. Soyer, J. Kirkpatrick, K. Kavukcuoglu, R. Pascanu, and R. Hadsell, "Progressive Neural Networks," arXiv:1606.04671, 2016.

[9] A. Mallya, D. Davis, and S. Lazebnik, "PackNet: Adding Multiple Tasks to a Single Network by Iterative Pruning," in CVPR, 2018.

[10] J. Serra, D. Suris, M. Miron, and A. Kalaitzis, "Overcoming Catastrophic Forgetting with Hard Attention to the Task," in ICML, 2018. (arXiv:1801.01423)

[11] S.-A. Rebuffi, A. Kolesnikov, G. Sperl, and C. H. Lampert, "iCaRL: Incremental Classifier and Representation Learning," in CVPR, 2017. (arXiv:1611.07725)

[12] D. Lopez-Paz and M. Ranzato, "Gradient Episodic Memory for Continual Learning," in NeurIPS, 2017. (arXiv:1706.08840)

[13] A. Chaudhry, M. Ranzato, M. Rohrbach, and M. Elhoseiny, "Efficient Lifelong Learning with A-GEM," in ICLR, 2019. (arXiv:1812.00420)

[14] C. Shin, W. C. J. Walker, and J. Si, "Continual Classification Learning Using Generative Models," in ICLR, 2019. (arXiv:1810.10612)

[15] N. Y. Kim, S. C. Kim, J. K. Park, Y. C. Lim, S. H. Lee, J. W. Lee, M. J. Lee, Y. S. Kim, K. R. Lee, H.-J. Yang et al., "Energy-Based Models for Continual Learning," in NeurIPS Workshop, 2020. (arXiv:2011.12216)

[16] R. Aljundi, M. Douillard, P. R. M. de Oliveira, and A. Calandra, "On Tiny Episodic Memories in Continual Learning," in ICML, 2019. (arXiv:1902.10486)

[17] A. C. I. Malibari, A. H. Alahdali, N. Alhokail, J. Park, D. Demarchi, and S. C. Perera, "Carousel Memory: Rethinking the Design of Episodic Memory for Continual Learning," in NeurIPS, 2021. (arXiv:2110.07276)

[18] S. I. Mirzadeh, M. Farajtabar, R. Pascanu, and H. Ghasemzadeh, "Understanding the Role of Training Regimes in Continual Learning," in NeurIPS, 2020. (arXiv:1912.02567)

[19] Y. K. M. Alve, S. Lee, J. Kim, and S. Yoon, "GRASP: A Rehearsal Policy for Efficient Online Continual Learning," arXiv:2308.13646, 2023.