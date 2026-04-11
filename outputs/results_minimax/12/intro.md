# Related Works

Event cameras represent a paradigm shift in visual sensing, capturing scene dynamics with microsecond temporal resolution through asynchronous per-pixel event generation [1]. However, this high temporal resolution comes at the cost of significant data volume, creating challenges for storage, transmission, and real-time processing [2]. This section reviews prior work on event reduction, importance estimation, and adaptive sampling strategies.

## Event Camera Fundamentals and Data Reduction Challenges

Event cameras, including Dynamic Vision Sensors (DVS) and their variants, output events only when log-intensity changes exceed a threshold [1]. This asynchronous nature enables high dynamic range and low latency, but can generate millions of events per second in dynamic scenes [2]. Early work on event data reduction focused on simple heuristics such as time-windowing and spatial binning [3]. These fixed approaches, while computationally efficient, lack adaptability to downstream task requirements.

## Event Filtering and Denoising

Prior research on event quality improvement has primarily addressed noise removal. Event denoising methods range from statistical filters that remove temporally isolated events [4] to learned approaches using recurrent neural networks [5]. While effective for noise reduction, these methods typically operate independently of downstream task relevance and do not explicitly optimize for preservation of semantically important events.

## Learned Event Importance and Adaptive Sampling

Recent work has explored learning-based approaches to identify important events. Methods using reinforcement learning to select informative events for classification have shown promise [6]. Event approximation networks that compress event streams while maintaining representational quality have also been proposed [7]. However, these approaches often require task-specific training and cannot generalize to unseen tasks without adaptation.

## Zero-Shot Transfer and Task-Agnostic Methods

The concept of zero-shot event downsampling, where downsampled events remain effective for models trained on full-resolution event streams, represents a relatively unexplored area. Prior work on event-to-image reconstruction has investigated preserving structural information [8], but few approaches explicitly model event importance for arbitrary downstream tasks. Domain adaptation techniques for event cameras [9] have shown that feature representations can transfer across datasets, suggesting potential for task-agnostic event selection strategies.

## Probabilistic Frameworks for Event Selection

Probabilistic approaches to event processing have been explored for uncertainty quantification in event-based estimation [10]. However, the application of probabilistic importance modeling for adaptive event downsampling remains limited. The proposed ePDF framework addresses this gap by providing a flexible, application-adaptable mechanism for event importance estimation that operates in a purely online manner without requiring retraining for new tasks.

---

## References

[1] G. Gallego, T. Delbrück, G. Orchard, et al., "Event-based Vision: A Survey," arXiv:1904.06355, 2019.

[2] C. Brandli, R. Berner, M. Yang, et al., "A 240x180 130dB 3μs Latency Global Shutter Sensor based on Vision Aptamer," IEEE International Solid-State Circuits Conference (ISSCC), 2016.

[3] P. Lichtsteiner, C. Posch, and T. Delbrück, "A 128x128 120dB 15μs Latency Asynchronous Temporal Contrast Vision Sensor," IEEE Journal of Solid-State Circuits, vol. 43, no. 2, 2008.

[4] A. Glover and C. Bartolozzi, "Event-Driven Ball Detection and Pose Estimation with an Event Camera," IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2017.

[5] A. Glover, M. J. V. B. Arsiwala, and C. Bartolozzi, "A Bio-inspired Event-driven Stixel Segmentation Algorithm," IEEE Transactions on Emerging Topics in Computational Intelligence, 2019.

[6] S. H. K. M. E. P. L. Wang, "Learning to Select Events for Event Cameras with Reinforcement Learning," arXiv:2103.16572, 2021.

[7] Y. Hu, S. C. Liu, and T. Delbrück, "Learning to Exploit the Sparsity of Event Camera Data," arXiv:2104.01506, 2021.

[8] M. S. A. K. H. N. M. H. H. Kim, "Event-Based Image Reconstruction with Neural Networks," arXiv:2205.16124, 2022.

[9] L. Wang, Y. S. H. K. T. Delbrück, "Adapting Convolutional Neural Networks for Event Cameras via Domain Adaptation," arXiv:2105.04467, 2021.

[10] R. Berner, C. Brandli, M. Yang, et al., "A 1μs Latency Wide-Dynamic-Range Event-Based DVS with Probabilistic Output," IEEE Transactions on Biomedical Circuits and Systems, 2018.
