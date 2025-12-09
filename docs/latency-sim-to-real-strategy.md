# Latency & Sim-to-Real Strategy

The goal of this course is to minimize the **Sim-to-Real Gap**—the performance degradation when a model trained in simulation is deployed to a physical robot. Managing **latency** is central to this strategy.

### The Sim-to-Real Strategy

1.  **Domain Randomization:** Training the AI model with varying parameters (lighting, textures, physics settings) within Isaac Sim to make the model robust to real-world variability.
2.  **Deployment Method:** Never stream control commands to a physical robot from a remote cloud instance. Always **download the trained model weights** (the AI "brain") and deploy them directly onto the local **Jetson Edge Kit**.
3.  **Local Control:** The Jetson runs the ROS 2 inference stack and the low-latency control loop for the robot locally. This ensures that perception and actuation commands execute fast enough (e.g., at 100 Hz) for bipedal balance.

### Summary of Architecture

| Component | Hardware | Function |
| :--- | :--- | :--- |
| **Sim Rig** | PC with RTX 4080 + Ubuntu 22.04 | Runs Isaac Sim, Gazebo, Unity, and trains LLM/VLA models. |
| **Edge Brain** | Jetson Orin Nano | Runs the **Inference** stack. Students deploy their code here for real-time operation. |
| **Sensors** | RealSense Camera + Lidar | Connected to the Jetson to feed real-world data to the AI. |
| **Actuator** | Unitree Go2 or G1 (Shared) | Receives low-level motor commands from the Jetson. |