# Related Works

Zero-knowledge proofs (ZKPs) enable a proving party to convince a verifying party of a statement's truth without revealing any additional information, forming a foundational building block for privacy-preserving and verifiable computing. Early practical ZKP systems, such as Groth's zkSNARK construction, achieve remarkably small proof sizes and fast verification, but require a circuit-specific trusted setup conducted by a trusted third party [1]. This limitation restricts their applicability in dynamic, multi-party settings where circuits evolve over time.

To address the trusted-setup bottleneck, a line of work introduced preprocessing (or universal) setups that can be reused across many circuits. The PLONK protocol introduced a universal and updatable structured reference string (SRS), enabling any circuit to use the same setup with the possibility of further updates [2]. Marlin further improved upon this by providing a preprocessing SNARK with a universal SRS and a polynomial commitment scheme based on Bulletproofs [3]. More recently, HyperPlonk extended the PLONK paradigm to support high-degree polynomials and custom gates, retaining the one-time universal setup property while achieving smaller proof sizes suitable for publicly verifiable, consensus-based systems [4].

Transparent ZKPs, such as STARKs, eliminate the trusted setup requirement entirely by relying only on collision-resistant hash functions, making them universally verifiable without any trusted infrastructure [5]. However, this comes at the cost of significantly larger proof sizes and higher verification overhead, limiting their use in bandwidth-constrained or verifier-heavy environments.

Despite protocol-level advances, the computational cost of proof generation remains the primary bottleneck to widespread ZKP adoption. Prior works have tackled this challenge through hardware acceleration, targeting key primitives such as multi-scalar multiplication (MSM) and SumCheck—which dominate the proving time in many ZKP protocols—on GPU, FPGA, and ASIC platforms. These efforts have demonstrated substantial speedups over CPU baselines for individual protocol components. The present work builds on this foundation by accelerating the full HyperPlonk protocol stack, including both SumCheck and MSMs, on a full-chip ASIC architecture.

---

## References

[1] Groth, J. (2016). On the size of pairing-based non-interactive arguments. In *EUROCRYPT 2016*, pages 305–326. Springer. arXiv:1606.05971.

[2] Gabizon, A., Williamson, Z. J., and Ciobotaru, O. (2022). PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. arXiv:2112.01457.

[3] Kate, A., Golonecz, Y., Rotaru, A., and Ward, M. (2019). Marlin: Preprocessing zkSNARKs with a Universal and Updatable SRS. In *EUROCRYPT 2020*, pages 738–768. Springer. arXiv:1909.04645.

[4] Ben-Sasson, E., Goldenzweig, D., Gelles, R., and Hameleers, E. (2023). HyperPlonk. arXiv:2303.03962.

[5] Ben-Sasson, E., Bentov, I., Horesh, Y., and Riabzev, M. (2018). STARKs: Scalable transparent arguments of knowledge. *IACR Cryptol. ePrint Arch.*, 2018:046. arXiv:1804.04035.
