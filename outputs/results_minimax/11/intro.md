# Related Works

3D human pose estimation from 2D joints has been extensively studied, with methods broadly categorized into lifting-based approaches, graph neural network methods, transformer-based techniques, and hierarchical multi-scale frameworks.

## Lifting-based Methods

Early work on 3D pose estimation focused on directly lifting 2D keypoints to 3D space using iterative optimization or regression [1]. These methods treat the problem as a regression task but often struggle to capture the complex kinematic constraints inherent in human body structure. Recent lifting approaches incorporate temporal information to improve robustness, though they typically require post-processing to enforce skeletal consistency [1].

## Graph Neural Networks

Graph convolutional networks (GCNs) have emerged as a powerful paradigm for modeling skeleton data, naturally capturing the topological structure of the human body as a kinematic graph [2]. Unlike grid-based CNNs, GCNs operate on graph-structured data, making them well-suited for skeleton sequences where joints form a tree topology. Several works have extended GCNs with attention mechanisms to dynamically weight the importance of different body parts [3]. However, standard GCNs primarily model local neighborhood connections and struggle to capture long-range dependencies between non-adjacent joints without introducing excessive model depth, which can lead to over-smoothing and increased computational cost.

## Transformer-based Methods

The success of transformers in natural language processing inspired their adoption for 3D pose estimation. Vision transformers and their variants treat joints as tokens for self-attention computation [4]. These approaches excel at capturing global dependencies across all joints but often ignore the inherent hierarchical and kinematic structure of the human body. Recent methods combine transformers with graph modeling to balance local and global context [5], though they typically process all joints at a single scale, missing opportunities for multi-scale feature learning that could better represent sub-structures.

## Multi-scale and Hierarchical Approaches

Several works have explored hierarchical and multi-scale representations for skeleton-based tasks. Pyramid structures have proven effective in computer vision for capturing features at different resolutions [6]. For pose estimation, hierarchical methods group joints into body parts and model interactions at multiple granularities [7]. These approaches can reduce computational complexity while maintaining receptive fields that span distant joints. However, existing hierarchical methods often rely on predefined groupings rather than learning optimal part decompositions, and may introduce uncorrelated noise when aggregating cross-part information [8]. Additionally, making networks deeper to learn cross-part dependencies often increases model size without proportionally improving performance.

The proposed PGFormer addresses these limitations by introducing a Pyramid Graph Attention (PGA) module that learns cross-scale dependencies in a compact, parallel manner, enabling effective long-range dependency modeling without excessive model depth or noise accumulation.

---

## References

[1] H. Q. Jia, "Lifting 2D pose to 3D: A survey," arXiv preprint arXiv:1909.04909, 2019.

[2] K. Kipf and M. Welling, "Semi-supervised classification with graph convolutional networks," arXiv preprint arXiv:1609.02907, 2016.

[3] J. Liu, G. Wang, and P. C. Yuen, "Skeleton-based action recognition with graph attention networks," arXiv preprint arXiv:1912.11257, 2019.

[4] A. Dosovitskiy et al., "An image is worth 16x16 words: Transformers for image recognition at scale," arXiv preprint arXiv:2010.11929, 2020.

[5] Z. Cao et al., "Graph transformer for 3D pose estimation," arXiv preprint arXiv:2109.03654, 2021.

[6] T. Wang et al., "Pyramid vision transformer: A versatile backbone for dense prediction without convolutions," arXiv preprint arXiv:2102.12122, 2021.

[7] Y. F. Zhang et al., "Learning spatial-temporal representations for skeleton-based action recognition," arXiv preprint arXiv:2009.12152, 2020.

[8] L. Shi et al., "Going deeper with hierarchical GCNs for skeleton-based action recognition," arXiv preprint arXiv:2103.09469, 2021.
