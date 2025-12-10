# Voice-to-Action: Integrating OpenAI Whisper

The convergence of large language models (LLMs) and robotics is rapidly shifting human-robot interaction from rigid, pre-programmed commands to **natural language instructions**. The first step in this Vision-Language-Action (VLA) pipeline is reliably converting human speech into text.

### The Role of OpenAI Whisper

**OpenAI Whisper** is a robust, general-purpose automatic speech recognition (ASR) model. Unlike older ASR systems, Whisper is highly accurate across various languages, accents, and background noise levels, making it ideal for a robotics lab environment.

### The Voice-to-Action Pipeline

1.  **Audio Capture:** The robot uses an onboard microphone array to capture the user's voice command (e.g., "Bring me the blue cup").
2.  **Transcription:** The audio is fed into the Whisper model (either running locally on an **NVIDIA Jetson** or via a cloud API), which outputs a precise text string: `"Bring me the blue cup."`
3.  **Command Parsing (The LLM Step):** This text string is then passed to the LLM (covered next) which interprets the intent and converts it into a machine-executable plan.
4.  **Error Handling:** Whisper's confidence scores can also be used to trigger confirmation requests if the model is unsure about the transcription, improving reliability.

**For the Capstone Project:** You will integrate a Python Whisper library to listen for a wake word, record a command, and then immediately pass that text to the LLM-Planner node in ROS 2.