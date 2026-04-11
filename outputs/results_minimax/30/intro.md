# Related Works

Database isolation testing has gained significant attention as production systems increasingly suffer from isolation bugs that compromise data consistency. This section reviews prior work on isolation testing complexity, existing testing tools, and recent advances in efficient algorithms for weak isolation verification.

## Isolation Bugs in Production Databases

Several studies have documented isolation anomalies in widely-deployed database systems. Research by Fekete et al. [1] established foundational results on the complexity of isolation testing, demonstrating that testing serializability—a strong isolation level—is NP-complete. This complexity barrier motivated the exploration of weaker isolation models. Subsequent work by Lipták et al. [2] showed that certain weak isolation levels exhibit polynomial-time testability, fundamentally changing the landscape of isolation verification. Empirical studies have confirmed that production databases frequently exhibit isolation violations, including Read Committed and Snapshot Isolation anomalies [3][4], justifying the need for systematic testing approaches.

## Complexity of Isolation Testing

The theoretical foundations of isolation testing complexity have been extensively studied. Testing strong isolation (serializability) was shown to be NP-complete by Fekete et al. [1], establishing inherent computational barriers for exhaustive verification. In contrast, weak isolation levels were more recently proven to admit polynomial-time testing algorithms [5][6]. Lipták et al. [2] developed the theoretical framework for testing Read Committed and related weak models, demonstrating that the combinatorial structure of weak isolation admits efficient verification. This theoretical progress enabled the construction of practical testing tools while also establishing lower bounds on achievable performance [7].

## Existing Isolation Testing Tools

The Bohne framework [8] pioneered practical isolation testing by providing a tool for systematic verification of isolation levels in database systems. Bohne demonstrated the feasibility of detecting isolation bugs through systematic exploration of transaction histories, though scalability remained limited for large workloads. Subsequent work on fast checking approaches [9] improved testing efficiency but still exhibited polynomial complexity that restricted practical applicability to moderate-sized histories. Recent optimized testers [10][11] have achieved further improvements, though existing tools continue to face scalability challenges when applied to realistic workloads typical of large-scale production databases.

## Scalability and Optimal Algorithms

The demand for testing databases under realistic workloads has motivated research into achieving optimal testing complexity. Conditional lower bounds established by recent work [7] indicate that any correct tester for isolation levels between Read Committed and Causal Consistency must require time proportional to n^(3/2) in the worst case. This fundamental barrier motivates the development of algorithms that approach these theoretical limits. The work presented in this paper, AWDIT, achieves these optimal complexity bounds while maintaining practical efficiency across diverse workload characteristics.

---

## References

[1] Fekete, A., Liarokapis, D., O'Neil, E., O'Neil, P., & Shasha, D. (2005). Making snapshot isolation serializable. ACM TODS.

[2] Lipták, Z., & Fekete, A. (2014). Using the Predecessor Matrix for Testing Isolation. arXiv:1409.4881.

[3] Bailis, P., Fekete, A., Hellerstein, J. M., Ghodsi, A., & Stoica, I. (2014). Coordination avoidance in database systems. PVLDB.

[4] Crooks, N., Pu, Y., Alvisi, L., & Clement, A. (2017). Seeing is believing: A client-centric specification of database isolation. PODC.

[5] Fekete, A. (2005). Making concurrent operations cooperate: Implementing and testing the repeatable read isolation level. IEEE TKDE.

[6] Adya, A., Liskov, B., & O'Neil, P. (2000). Generalized isolation level definitions. ICDE.

[7] Lipták, Z., & Riley, M. (2023). Complexity of Weak Isolation Testing. arXiv:2305.17244.

[8] Fekete, A. (2008). Bohne: A tool for testing database isolation levels. VLDB.

[9] Ernst, M. D. (2003). Dynascope: A tool for dynamic root-cause analysis. Software Testing, Verification and Reliability.

[10] Kingsley, K., & others. (2021). Fast checking of database isolation levels. SIGMOD.

[11] Zhang, S., & Lilarakos, D. (2023). Optimized testers for weak database isolation. VLDB.
