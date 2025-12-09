# RTX Workstation Requirements

This section details the specific requirements for the **"Digital Twin" Workstation** necessary to run the core simulation and training environments.

## GPU (The Bottleneck)

* **Minimum:** NVIDIA RTX 4070 Ti (12GB VRAM).
* **Why:** You need high VRAM to load the **USD (Universal Scene Description)** assets for the robot and environment, plus run the large **VLA (Vision-Language-Action)** models simultaneously.
* **Ideal:** RTX 3090 or 4090 (24GB VRAM). This level of power allows for much smoother **Sim-to-Real** training loops and development.

## CPU, RAM, and OS

* **CPU:** Intel Core i7 (13th Gen+) or AMD Ryzen 9. Physics calculations (Rigid Body Dynamics) in Gazebo and Isaac Sim are highly **CPU-intensive**.
* **RAM:** **64 GB DDR5** is strongly recommended. While 32 GB is the absolute minimum, it will likely lead to crashes during complex scene rendering or large model loading.
* **Operating System:** **Ubuntu 22.04 LTS**. Although Isaac Sim runs on Windows, ROS 2 is native to Linux. Dedicated Linux machines or reliable dual-boot setups are mandatory for a consistent developer experience.