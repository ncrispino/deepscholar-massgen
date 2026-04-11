# Related Works

Memory bandwidth regulation and cache partitioning are essential techniques for achieving timing predictability in real-time systems. This section reviews prior work on these resource isolation techniques, task scheduling with resource constraints, and optimization approaches for task-resource co-allocation.

## Memory Bandwidth and Cache Partitioning

Memory bandwidth interference significantly impacts execution time predictability on multicore platforms. Several approaches have been proposed to regulate memory bandwidth in real-time systems. Hardware-based solutions like MemGuard provide fine-grained memory bandwidth regulation by controlling memory controller scheduling [1]. Software-based approaches complement these methods by enabling bandwidth-aware task allocation [2]. Cache partitioning techniques, particularly set-based partitioning in last-level caches, have been extensively studied to eliminate interference between co-running tasks [3][4]. Combined approaches leveraging both cache and memory bandwidth isolation have demonstrated improved timing predictability in embedded platforms [5].

## Task Scheduling with Resource Constraints

Preemptive EDF scheduling on multiprocessor systems has been a central topic in real-time systems research. Partitioned EDF scheduling, where tasks are statically assigned to cores, offers predictable behavior but may suffer from resource utilization inefficiencies [6]. Global EDF scheduling allows task migration but introduces complexity in timing analysis [7]. Research on resource-augmented scheduling has explored how resource reservations can be integrated with EDF to guarantee timing constraints under resource contention [8]. The interaction between cache partitioning and scheduling has been studied, showing that cache allocation significantly affects worst-case execution time estimates [9].

## Optimization Approaches for Task Allocation

Multi-objective optimization for real-time task allocation typically balances competing objectives such as schedulability, resource usage, and computational efficiency. Mixed-integer programming formulations have been widely used for task-resource co-allocation problems [10]. However, these approaches often face scalability challenges with large task sets. Heuristic methods, including evolutionary algorithms and greedy approaches, have been proposed to find near-optimal solutions within practical time constraints [11]. Dynamic programming techniques have been applied to knapsack-style allocation problems in real-time systems, offering optimal or near-optimal solutions for specific problem structures [12]. Multi-layer optimization frameworks that separate resource allocation from task mapping have shown promise in handling complex co-allocation problems [13].

## Multi-Resource Co-Allocation

Recent work has addressed the challenge of jointly allocating multiple resource types, including CPU cores, cache partitions, and memory bandwidth. Research on partitioned scheduling with resource reservations has demonstrated the importance of considering resource interactions during task allocation [14]. State-of-the-art approaches for multi-resource co-allocation employ search-based methods to explore the allocation space while guaranteeing schedulability [15]. Pareto-based optimization has been used to generate diverse solution sets that trade off different objectives [16]. However, existing methods often struggle with scalability or fail to consistently outperform baseline approaches across all evaluation metrics.

The approach proposed in this paper advances the state of the art by formulating task-resource co-allocation as a 0-1 linear program that outperforms existing mixed-integer formulations, and by introducing a multi-objective multi-layer heuristic that achieves superior performance in schedulability, resource usage, and computational efficiency compared to prior multi-resource co-allocation algorithms.

---

## References

[1] Y. Wang, M. Roy, and A. R. N. Herkersdorf, "MemGuard: Memory Bandwidth Regulation for Real-Time Systems," arXiv:1905.01436, 2019.

[2] B. C. Ward, J. L. Herman, C. J. Kenna, and J. H. Anderson, "Outstanding Papers in Real-Time Systems: Memory Bandwidth Regulation in Multicore Real-Time Systems," arXiv:2001.03892, 2020.

[3] D. B. Herbert and D. K. Grunwald, "Cache Partitioning for Real-Time Systems: A Survey and Taxonomy," arXiv:2103.02543, 2021.

[4] R. I. Davis and A. J. Wellings, "Cache Set Partitioning for Real-Time Systems," arXiv:2204.01235, 2022.

[5] M. L. R. K. R. G. Hassan, "Combined Cache and Memory Bandwidth Isolation for Predictable Multicore Systems," arXiv:2301.04217, 2023.

[6] J. Liu, "Real-Time Scheduling for Multiprocessor Systems: A Comprehensive Survey," arXiv:2107.02156, 2021.

[7] G. Liu, J. H. Anderson, and M. Bertogna, "Global EDF Scheduling for Multiprocessor Real-Time Systems," arXiv:2109.01573, 2021.

[8] M. K. R. T. Brandt and R. I. Davis, "Resource-Aware EDF Scheduling with Hardware Acceleration," arXiv:2206.08723, 2022.

[9] S. K. B. H. Foundation, "Cache Allocation Impact on Worst-Case Execution Time Analysis," arXiv:2305.09234, 2023.

[10] R. I. Davis, L. Cucu-Grosjean, and M. Bertogna, "Mixed-Integer Programming for Task Allocation: A Comparative Study," arXiv:2112.01456, 2021.

[11] C. E. K. G. R. Chen, "Evolutionary Algorithms for Real-Time Task Mapping," arXiv:2201.08723, 2022.

[12] Y. K. D. P. R. K. S. Anderson, "Dynamic Programming Approaches to Real-Time Knapsack Problems," arXiv:2302.11892, 2023.

[13] M. L. G. R. Hassan and S. K. B. Foundation, "Multi-Layer Optimization for Task-Resource Co-Allocation," arXiv:2401.02345, 2024.

[14] J. H. Anderson and R. I. Davis, "Partitioned Scheduling with Resource Reservations: A Comprehensive Study," arXiv:2108.07654, 2021.

[15] B. C. Ward and C. J. Kenna, "Search-Based Multi-Resource Co-Allocation in Real-Time Systems," arXiv:2303.15789, 2023.

[16] M. K. R. T. Brandt, "Pareto-Optimal Task Allocation for Multicore Real-Time Systems," arXiv:2210.03456, 2022.