# Lab Architecture: On-Premise vs. Cloud

Building a "Physical AI" lab requires a choice between a high initial investment (**On-Premise/On-Campus**) or high recurring costs (**Cloud-Native**).

## Option 1: High CapEx (On-Premise Lab)

* **Structure:** Each student has a dedicated **RTX Workstation** (Sim Rig) and their own **Jetson Edge Kit** (Edge Brain). Robots are shared resources.
* **Pros:** Zero network latency for development, predictable long-term costs, full control over the environment.
* **Cons:** High initial cost (CapEx), ongoing maintenance of hardware and OS.

## Option 2: High OpEx (Cloud-Native Lab)

* **Structure:** Students rent **Cloud Workstations** (e.g., AWS g5.2xlarge with A10G GPU) to run Isaac Sim and training loops. They only own the **Edge Kit** and **Sensors** locally.
* **Cloud Instance Cost:** Approximately ~$1.50/hour. For a 12-week course (120 hours total usage), the cost is ~$205 per student per quarter, plus storage.
* **Pros:** Rapid deployment, suitable for students with underpowered personal laptops.
* **Cons:** **Latency** is a critical issue for real-time control (see Latency Trap), and the costs are recurring.

### Latency Trap (Critical Warning)

Training models in the cloud works well, but **controlling a real, physical robot from a cloud instance is dangerous and impractical due to network latency**.

**The Solution:** Students **train** models in the cloud, then **download the model weights** and **flash them to their local Jetson kit**. The Jetson then controls the physical robot locally.