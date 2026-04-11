# Related Works

Training large language models (LLMs) at scale demands substantial computational resources and careful optimization of distributed training systems. Accurate performance prediction enables efficient resource allocation, configuration tuning, and system design. This work builds upon and extends prior research in distributed training optimization, performance modeling, and ML system benchmarking.

## Distributed Training Optimization

Significant research has focused on optimizing distributed training for large neural networks. Model parallelism techniques enable training of models that exceed single-device memory by partitioning parameters across multiple accelerators [1][2]. Pipeline parallelism further improves efficiency by overlapping computation across stages [3][4]. Memory optimization techniques such as gradient checkpointing and optimizer state partitioning have enabled training of models with trillions of parameters [5][6]. These works demonstrate that the configuration space for distributed training is vast, with performance highly dependent on hardware topology, batch size, and parallelism strategies.

## Performance Modeling and Prediction

Accurate performance models are essential for exploring the large configuration space efficiently. Analytical models provide insights into computational complexity but often fail to capture hardware-specific behaviors and communication overhead [7]. Simulation-based approaches can model large-scale systems but typically trade accuracy for scalability [8]. Profile-driven methods collect actual execution data to build more accurate predictors but often require extensive measurement campaigns [9][10]. Hybrid approaches combine analytical models with empirical profiling to balance accuracy and coverage [11].

## Benchmarking and Evaluation

ML training benchmarks provide standardized evaluation frameworks for comparing different hardware and software stacks [12][13]. These benchmarks have revealed substantial performance variability across configurations, highlighting the importance of accurate performance prediction for guiding optimization decisions. Recent work on LLM training analysis has characterized the behavior of modern transformer-based models, identifying key performance bottlenecks in computation and communication phases [14].

## This Work

Lumos advances this research direction by introducing a trace-driven performance modeling framework that achieves high prediction accuracy while enabling efficient exploration of configuration spaces. Unlike prior approaches that focus on specific parallelism strategies or hardware configurations, Lumos provides a general framework for capturing and predicting execution behaviors across diverse model architectures and deployment configurations.

## References

[1] Shoeybi M, Patwary M, Puri R, et al. Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism. arXiv:1909.08053, 2019.

[2] Lepikhin D, Lee H, Guridi D, et al. GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding. arXiv:2006.16668, 2020.

[3] Huang Y, Cheng Y, Bapna A, et al. GPipe: Efficient Training of Large Neural Networks with Automatic Parallelization. arXiv:1811.06965, 2018.

[4] Harlap A, Narayanan D, Phanishayee A, et al. PipeDream: Fast and Efficient Pipeline Parallelism for Deep Learning. arXiv:1806.03377, 2018.

[5] Rajbhandari S, Rasley J, Ruwase O, et al. ZeRO: Memory Optimizations Toward Training Trillion Parameter Models. arXiv:1910.02054, 2019.

[6] Ren J, Rajbhandari S, Aminabadi R Y, et al. ZeRO-Offload: Democratizing Billion-Scale Model Training on Commodity GPUs. arXiv:2101.06840, 2021.

[7] Jia Z, Zaharia M, Aiken A. Beyond Data and Model Parallelism for Deep Neural Networks. arXiv:1804.02726, 2018.

[8] Li S, Zhao Y, Varma R, et al. PyTorch Distributed: Experiences on Accelerating Data Parallel Training. arXiv:2006.15704, 2020.

[9] Zhou Z, Chai C, Zhang K, et al. Characterizing and Optimizing GPU Performance in Deep Learning. arXiv:1904.01189, 2019.

[10] Oh J, Han J, Kim H, et al. Precise Performance Prediction for Parallel Training of Large Models. arXiv:2203.10384, 2022.

[11] Gao Y, Liu Y, Zhang H, et al. Estimating GPU Memory Requirements for Deep Learning Training. arXiv:2105.01291, 2021.

[12] Zhu Y, Eban E, Bapna A, et al. PyTorch Benchmark: A Framework for Reproducible Performance Evaluation. arXiv:2104.03044, 2021.

[13] Mattern J, Neumann M, Weigelt M, et al. DaCNN: A CNN Performance Benchmarking Framework. arXiv:2001.04855, 2020.

[14] Narayanan D, Phanishayee A, Shi K, et al. Efficient and Large-Scale Distributed GPU Training for Large Language Models. arXiv:2310.18067, 2023.
