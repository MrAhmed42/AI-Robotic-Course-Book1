# On-Premise vs. Cloud Lab Comparison

Choosing the lab model dictates the budget and student experience.

| Feature | On-Premise Lab (High CapEx) | Cloud-Native Lab (High OpEx) |
| :--- | :--- | :--- |
| **Initial Cost** | **Very High** (Purchase of all RTX PCs/Jetsons) | Low (Only purchase Edge Kits) |
| **Recurring Cost** | Low (Electricity, minimal software) | **High** (Hourly rental fees for GPU instances) |
| **Latency** | **Zero** (Local development) | Significant (Poor for real-time control/debugging) |
| **Ideal For** | Institutions with capital; students needing fast, local simulation. | Students with weak personal hardware; rapid, temporary scaling needs. |
| **Best Practice** | Train locally on RTX PCs; deploy to local Jetson Edge Kit. | Train on cloud instance; download model weights and flash to local Jetson Kit for deployment. |