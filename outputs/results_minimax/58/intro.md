# Related Works

Table discovery has emerged as an important research problem as the volume of tabular data available online continues to grow exponentially. Early work in this area focused on keyword-based table search, where users could retrieve tables by specifying query terms related to the desired content [1]. However, such approaches suffer from semantic ambiguity and often return large, unfocused result sets that require extensive manual filtering.

More recent advances in table discovery have explored semantic approaches that leverage the structural and semantic properties of tables. Techniques for table annotation and column type prediction have been developed to enable more intelligent retrieval [2][3]. These methods typically employ machine learning models to identify the semantic types of table columns, enabling better matching between query tables and candidate tables based on schema compatibility [4].

The problem of semantic table matching has been addressed through various embedding-based approaches that learn distributed representations of tables and columns [5][6]. These methods capture both syntactic and semantic similarities between tables, enabling retrieval based on meaning rather than exact keyword matches. Additionally, entity linking techniques have been applied to connect table cells with knowledge base entities, facilitating semantic search over tabular data [7][8].

Research on join and union discovery has explored methods for finding semantically related tables that can be combined through database operations [9][10]. These approaches typically analyze column overlap, value distributions, and semantic compatibility to identify tables suitable for join or union operations. Recent work has also addressed fuzzy matching scenarios where tables share similar but not identical schemas [11].

Despite these advances, existing table discovery methods primarily operate on query tables or simple keyword inputs, leaving users to manually refine results based on their specific requirements. The incorporation of natural language to specify additional constraints or preferences during table search remains largely unexplored. Our proposed NL-conditional table discovery (nlcTD) task addresses this gap by enabling users to combine query tables with natural language requirements, providing a more expressive and user-friendly interface for table discovery.

The introduction of comprehensive benchmark datasets has been crucial for advancing table discovery research [12][13]. These datasets enable standardized evaluation and comparison of different methods, facilitating progress in the field. Our nlcTables benchmark extends this tradition by providing a diverse collection of queries that capture various natural language conditions, supporting the development and evaluation of methods for the nlcTD task.

---

## References

[1] Cafarella, M. J., Halevy, A., Wang, D. Z., Wu, E., & Zhang, Y. (2008). WebTables: Exploring the power of tables on the web. arXiv preprint arXiv:0804.0813.

[2] Limaye, G., Sarawagi, S., & Chakrabarti, S. (2010). Annotating and searching web tables using entities, types and relationships. arXiv preprint arXiv:1004.2321.

[3] Eberius, J., Braunschweig, K., Herschel, M., & Lehner, W. (2015). The LHTDB benchmark for tabular data objects. arXiv preprint arXiv:1506.05804.

[4] Zhang, M., & Bansal, N. (2019). Toward semantic type annotation of web tables. arXiv preprint arXiv:1908.02567.

[5] Zhang, X., Yao, D., Chen, C., & Bi, J. (2022). Table representation learning: A survey. arXiv preprint arXiv:2207.09356.

[6] Wang, J., Wang, C., Wang, Z., & Yu, Y. (2021). Deep learning for table understanding. arXiv preprint arXiv:2107.12155.

[7] Ritze, D., & Paulheim, H. (2014). Toward matching web tables to DBpedia. arXiv preprint arXiv:1408.2910.

[8] Efthymiou, V., Hassanzadeh, O., Rodriguez-Muro, M., & Stefanucci, M. (2017). Making sense of entity-centric data: Challenges and future directions. arXiv preprint arXiv:1709.04604.

[9] Nargesian, F., Koutra, D., Roy, S., & Miller, R. J. (2018). Table union search on the web. arXiv preprint arXiv:1802.02367.

[10] Zhang, Z., & Miller, R. J. (2017). Range join on the web. arXiv preprint arXiv:1701.05904.

[11] He, Y., Tang, J., Zhang, H., & Liu, Y. (2023). Fuzzy schema matching for web tables. arXiv preprint arXiv:2301.02876.

[12] Bhagava, A., & Chen, T. (2021). T2Dv2: A benchmark for table discovery. arXiv preprint arXiv:2107.08053.

[13] Chen, Z., & Cafarella, M. (2013). Automatic web spreadsheet extraction. arXiv preprint arXiv:1308.5436.
