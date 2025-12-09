# The "Physical AI" Edge Kit (Jetson Setup)

The Edge Kit serves as the **"Physical AI" Brain**—the nervous system of the robot that runs the AI models in real-time. This covers the deployment phase in Module 3 (Isaac ROS) and Module 4 (VLA).

### Core Components

| Component | Model | Approximate Price | Role and Function |
| :--- | :--- | :--- | :--- |
| **The Brain** | **NVIDIA Jetson Orin Nano (8GB)** or NX (16GB) | ~$249 (Nano) | The industry standard for embodied AI. Students deploy their trained ROS 2 nodes here to understand resource constraints. |
| **The Eyes** | **Intel RealSense D435i** or D455 | $349 | Provides RGB (Color) and Depth (Distance) data. Essential for the VSLAM and Perception modules. The 'i' model includes an onboard IMU. |
| **The Ears** | ReSpeaker USB Mic Array v2.0 | $69 | Far-field microphone array necessary for the "Voice-to-Action" **Whisper** integration (Module 4). |
| **Balance** | Generic USB IMU (BNO055) | Low | While IMUs are often built-in, a separate module helps teach critical IMU calibration and data fusion. |
| **Storage** | SD Card (128GB) + Power | $30 | High-endurance microSD card required to run the operating system and store model weights. |
| **Total Per Kit** | | **~$700** | This is the minimum cost to teach the deployment phase of Physical AI. |