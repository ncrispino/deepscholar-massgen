# Related Works

Graph Convolutional Networks (GCNs) have become a cornerstone for modern collaborative filtering (CF) systems. The seminal work by Kipf and Welling [1] introduced the concept of spectral graph convolutions for semi-supervised classification, which laid the theoretical foundation for subsequent graph-based recommendation models. Building upon this framework, Wang et al. [4] proposed Neural Graph Collaborative Filtering (NGCF), which explicitly models the collaborative signal in user-item interaction graphs through graph convolutional operations. NGCF demonstrated that explicitly injecting the recommendation task into graph embedding learning significantly improves recommendation quality compared to traditional matrix factorization approaches.

However, the simplification introduced by He et al. [3] revealed that many architectural components in standard GCNs are unnecessary for collaborative filtering. LightGCN retains only the essential neighbor aggregation mechanism while removing feature transformation and nonlinear activation operations. This simplification not only reduces model complexity but also improves performance, suggesting that the original GCN architecture contains components that may be suboptimal for the CF domain. Wu et al. [5] further demonstrated that simplified graph neural networks can maintain competitive performance with substantially reduced computational overhead.

Spectral graph theory provides a principled foundation for understanding graph filtering operations. Defferrard et al. [2] introduced Chebyshev spectral filtering, which approximates graph convolutions using Chebyshev polynomials to achieve computationally efficient localized filtering. This approach enables the design of filters with arbitrary frequency responses while maintaining linear complexity with respect to graph size. The Chebyshev approximation avoids the explicit eigendecomposition required by full spectral methods, making it practical for large-scale applications.

Recent work has also explored limitations of embedding-based approaches in recommendation systems. The latent space constraints imposed by fixed embedding dimensions can limit the model's capacity to capture diverse user preference patterns, particularly for users with extensive interaction histories. Additionally, neighborhood aggregation in standard GCNs treats all neighbors equally, potentially missing fine-grained variations in collaborative signals. These observations motivate the development of spectral filtering approaches that can operate directly on raw interaction patterns without the representational constraints of learned embeddings.

The proposed ChebyCF framework addresses these challenges by leveraging spectral graph theory to overcome the frequency cut-off limitations of existing GCN-based CF methods. By combining Chebyshev interpolation with ideal pass filters and degree-based normalization, ChebyCF achieves a more flexible frequency response that can capture the full spectrum of collaborative signals in user-item interactions.

# References

[1] Kipf TN, Welling M. Semi-supervised classification with graph convolutional networks. arXiv. 2016. arXiv:1609.02907.

[2] Defferrard M, Bresson X, Vandergheynst P. Convolutional neural networks on graphs with fast localized spectral filtering. arXiv. 2016. arXiv:1606.09375.

[3] He X, Deng K, Wang X, Li Y, Zhang Y, Zhuang M. LightGCN: Simplifying and powering graph convolution network for recommendation. arXiv. 2020. arXiv:2002.02126.

[4] Wang X, He X, Wang M, Feng F, Chua TS. Neural graph collaborative filtering. arXiv. 2019. arXiv:1905.04413.

[5] Wu F, Souza A, Zhang T, Fifty C, Yu T, Weinberger K. Simplifying graph neural networks. arXiv. 2019. arXiv:1905.09550.
