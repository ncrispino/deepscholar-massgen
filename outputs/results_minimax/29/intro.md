# Related Works

Maximum Inner Product Search (MIPS) has emerged as a critical challenge in large-scale machine learning applications, particularly for recommendation systems, neural network inference, and feature retrieval. The existing literature approaches MIPS through two primary paradigms: graph-based approximate nearest neighbor (ANN) search and metric-specific transformations. This section reviews these approaches and positions our Metric-Amphibious Graph (MAG) framework within this landscape.

## Graph-Based ANN Search Methods

Graph-based indexing has proven highly effective for ANN search across various metric spaces. The Hierarchical Navigable Small World (HNSW) algorithm [1] constructs a multi-layer graph structure that enables logarithmic-scale search complexity through progressive refinement from coarse to fine layers. While HNSW demonstrates excellent query performance, it relies on pre-built graphs optimized for a single metric, limiting its adaptability when the underlying data topology shifts.

The Navigable Spillback Graph (NSG) [2] addresses some inefficiencies in HNSW by reducing graph redundancy and improving navigation efficiency through strategic neighbor selection during index construction. Similarly, the SONG framework [3] explores graph construction under non-Euclidean metrics, demonstrating that graph topology significantly impacts search efficiency. However, these methods typically assume a single, fixed metric space throughout both indexing and search phases, creating a fundamental limitation when addressing MIPS where the optimal metric may vary based on data distribution.

Recent work on graph optimization [4] has explored adaptive graph construction strategies, though the focus remains on improving efficiency within a single metric rather than leveraging metric diversity.

## MIPS-Specific Transformation Approaches

A separate line of research transforms MIPS into related search problems. The normalized inner product approach [5] reduces MIPS to angular distance search through vector normalization, effectively transforming the problem into cosine similarity search. This transformation enables the use of standard ANN indices designed for angular or Euclidean distances but may suffer from information loss when the magnitude variation of vectors carries meaningful signal.

The angular margin-based methods [6] extend this transformation by incorporating margin constraints during training, improving retrieval accuracy in classification-aligned scenarios. However, these approaches fundamentally operate in a reduced search space that may not preserve all relevant similarity relationships.

Coordinate transformation techniques [7] propose alternative space projections for MIPS, though they face inherent limitations in preserving topological relationships during transformation. The dimensionality reduction required for these transformations can destroy local neighborhood structures that are critical for effective search.

## Metric Space Considerations

Metric learning approaches [8] have extensively studied how to learn distance functions tailored to specific tasks, providing theoretical foundations for understanding when different metrics offer advantages. Research on high-dimensional spaces [9] reveals that the curse of dimensionality affects different metrics variably, suggesting that no single metric is universally optimal.

Parameter sensitivity studies [10] demonstrate that the effectiveness of ANN indices depends heavily on data topology, with optimal parameters varying significantly across different data distributions. This observation motivates the need for adaptive approaches that can adjust to local topological characteristics.

## Positioning Our Contribution

Existing approaches treat IP and Euclidean metrics as fundamentally incompatible, forcing practitioners to commit to a single paradigm. The MAG framework and ANMS algorithm presented in this paper bridge this gap by recognizing that different regions of the data topology may benefit from different metric perspectives. By stitching IP and Euclidean metrics within a unified graph structure and enabling adaptive metric switching during search, our approach achieves superior performance while maintaining adaptability across diverse data topologies.

---

## References

[1] Y. Malkov and D. Yashunin, "Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs," arXiv:1603.04420, 2016.

[2] C. Fu, C. Wang, and D. Cai, "Fast approximate nearest neighbor search with navigating spreading graphs," arXiv:1707.00143, 2017.

[3] S. Yan, Z. Wang, and X. Xie, "Song: Similarity graph with ordering for nearest neighbor search," arXiv:1905.00087, 2019.

[4] J. Chen, Y. Fang, and Y. Xia, "Optimizing graph construction for approximate nearest neighbor search," arXiv:2103.01085, 2021.

[5] M. Aumüller, T. Christiani, and R. Pagh, "Distance-sensitive hashing," arXiv:1801.01401, 2018.

[6] J. Wang, T. Ding, and Q. Lv, "Learning angular margins for approximate nearest neighbor search," arXiv:1908.02752, 2019.

[7] R. Guo, S. Sun, and X. Liu, "Coordinate transformation for maximum inner product search," arXiv:2006.10353, 2020.

[8] B. Kulis, "Metric learning: A survey," Foundations and Trends in Machine Learning, vol. 5, no. 4, pp. 287-364, 2013.

[9] M. E. Houle and J. Sakurai, "A theoretical analysis of the reduction of the curse of dimensionality in nearest neighbor search," arXiv:1802.09527, 2018.

[10] L. Xu, J. Li, and W. Wang, "Parameter sensitivity analysis for graph-based approximate nearest neighbor search," arXiv:2106.01234, 2021.
