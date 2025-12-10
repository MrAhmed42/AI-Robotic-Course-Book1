# Hardware Requirements: Course Demands

This course is exceptionally demanding, sitting at the intersection of **Physics Simulation**, **Visual Perception**, and **Generative AI**. Because the Capstone involves a **Simulated Humanoid**, significant computational power is required.

The architecture is split into two primary investment areas:

1.  **The "Digital Twin" Workstation** (High-Performance PC)
2.  **The "Physical AI" Edge Kit** (Onboard Robot Brain)

### 1. The "Digital Twin" Workstation (Required per Student)

This is the most critical component, necessary for running NVIDIA Isaac Sim, an Omniverse application that requires Ray Tracing (**RTX**) capabilities. Standard laptops will not suffice.

| Component | Minimum Specification | Ideal Specification | Notes |
| :--- | :--- | :--- | :--- |
| **GPU** | **NVIDIA RTX 4070 Ti (12GB VRAM)** | RTX 3090 or 4090 (24GB VRAM) | **The Bottleneck:** High VRAM is required to load USD assets for the robot/environment and run large VLA models simultaneously. |
| **CPU** | Intel Core i7 (13th Gen+) or AMD Ryzen 9 | Latest generation high-core count | Physics calculations (Rigid Body Dynamics) in Gazebo/Isaac are CPU-intensive. |
| **RAM** | 64 GB DDR5 | 64 GB+ | 32 GB is the absolute minimum, but often crashes during complex scene rendering. |
| **OS** | **Ubuntu 22.04 LTS** | Ubuntu 22.04 LTS | ROS 2 (Humble/Iron) is native to Linux. Dual-booting or dedicated Linux machines are mandatory for a friction-free experience. |