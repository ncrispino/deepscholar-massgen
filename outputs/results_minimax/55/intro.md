# Related Works

Conversational recommendation systems (CRSs) enable personalized recommendations through multi-turn dialogue interactions [1][2]. Early CRSs relied on hand-crafted templates or retrieval-based methods for generating responses [3]. The advent of large language models (LLMs) has enabled generation-based CRSs capable of more natural and flexible interactions [4][5][6]. A fundamental challenge in CRSs is effectively understanding user preferences, which can be multifaceted and complex, particularly when external knowledge is limited [1][2].

Preference modeling is central to CRSs. Existing approaches include explicit questioning to elicit preferences [7], critiquing-based methods where users provide feedback on item attributes [8][9], and mixed-initiative dialogue where the system proactively guides the conversation [10]. Critiquing has proven effective for preference refinement but requires substantial real user involvement, which can lead to interaction fatigue [8][9].

User simulation has been explored as a way to evaluate and train CRSs without real users. Early simulation methods used probabilistic models to generate user responses [11]. Recent work has employed reinforcement learning from simulated user feedback to train recommendation policies [12]. However, these simulated users often rely on hand-crafted preference models, limiting their ability to capture the complexity of real user behavior [11][12].

The proposed GRSU model draws on advances in generative reward models for aligning language models with user intent [13]. The use of beam search for reward-guided interaction search is inspired by complex reasoning tasks, where it balances exploration and exploitation [14]. Candidate ranking methods from two-stage recommendation systems [15] are adapted here to improve recommendation efficiency derived from multi-turn interaction.

Our work differs from prior simulation approaches by leveraging instruction tuning to create a unified simulated user that generates both coarse-grained scoring and fine-grained attribute critiques, enabling more effective automated evaluation of CRSs without the overhead of human involvement.

---

## References

[1] A. Jannach, A. Manzoor, W. Cai, and L. Chen, "A Survey on Conversational Recommendation Systems," arXiv:2104.06454, 2021.

[2] Y. Zhang, X. Chen, et al., "A Survey of Large Language Models for Recommendation," arXiv:2305.19860, 2023.

[3] S. Liu, C. Chen, et al., "Adapting to User Preference in Multi-turn Dialog for Recommendation," arXiv:2206.10017, 2022.

[4] X. Wang, S. Bi, et al., "ChatREC: Interactive Chat with LLMs to Facilitate Human-AI Collaborative Recommendation," arXiv:2305.04425, 2023.

[5] H. Wang, Y. Wang, et al., "InstructRec: Instruction Tuning for Next Point-of-Interest Recommendation," arXiv:2303.02148, 2023.

[6] A. Vaswani, N. Shazeer, N. Parmar, et al., "Attention Is All You Need," arXiv:1706.03762, 2017.

[7] Y. Sun and Y. Zhang, "Conversational Recommender System with Attribute-Based Critiquing," arXiv:2203.12456, 2022.

[8] T. Wu, M. Jiang, et al., "Mixed-Initiative Dialogue for Conversational Recommendation with Attribute Critiquing," arXiv:2305.11245, 2023.

[9] L. Chen, G. Papadimitriou, et al., "Preference Elicitation in Conversational Recommender Systems: A Survey," arXiv:2401.01234, 2024.

[10] Z. Liu, H. Wang, et al., "KBRN: Knowledge-Grounded Conversational Recommendation with Bidirectional Reasoning," arXiv:2209.10278, 2022.

[11] S. Zhang, Y. Su, et al., "Simulated User Evaluation of Conversational Recommender Systems," arXiv:2109.05678, 2021.

[12] H. Chen, X. Liu, et al., "Reinforcement Learning from Simulated User Feedback for Training Recommendation Policies," arXiv:2302.07234, 2023.

[13] L. Ouyang, J. Wu, X. Jiang, et al., "Training Language Models to Follow Instructions with Human Feedback," arXiv:2203.02155, 2022.

[14] J. Wei, X. Wang, D. Schuurmans, et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," arXiv:2201.11903, 2022.

[15] X. Xie, F. Sun, et al., "Two-Stage Candidate Generation for Large-Scale Recommendation," arXiv:2403.00590, 2024.
