# Robot Lab Options (The Actuator)

To teach "Physical AI," you must eventually address the hardware. Since a full humanoid is prohibitive, we offer three tiers of options for the **Actuator** (the body) depending on budget and educational goals.

### Option A: The "Proxy" Approach (Recommended for Budget)

* **Robot:** **Unitree Go2 Edu** (~$1,800 - $3,000).
* **Pros:** Highly durable, excellent ROS 2 support, and significantly more affordable than humanoids. The software principles (ROS 2, VSLAM, Isaac Sim) transfer 90% effectively.
* **Cons:** Not a biped (humanoid).

### Option B: The "Miniature Humanoid" Approach

* **Robot:** **Unitree G1** (~$16,000) or older, stable platforms like the **Robotis OP3** (~$12,000).
* **Budget Alternative Warning:** Cheaper kits (e.g., Hiwonder TonyPi Pro) usually run on Raspberry Pi, which cannot run the NVIDIA Isaac ROS stack efficiently. These are only useful for kinematics and should be paired with the Jetson Kit for AI.

### Option C: The "Premium" Lab (Sim-to-Real Specific)

* **Robot:** **Unitree G1 Humanoid**.
* **Goal:** The primary option if the objective is to deploy the Capstone project directly to a real, dynamically walking bipedal platform. This requires the highest level of budget and expertise.