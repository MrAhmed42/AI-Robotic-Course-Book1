# Physics Simulation in Gazebo

## Overview
Digital Twin development begins by creating a realistic simulation of the physical world.  
Gazebo is the primary physics simulator used in robotics because it is fast, accurate, and supports real-time interaction.

This chapter explains:
- How physics works inside Gazebo  
- Gravity, collisions, friction  
- How robots move and respond to forces  
- Why accurate physics is important for a Digital Twin

---

## Understanding Gazebo Physics Engine
Gazebo uses physics engines such as:
- **ODE**
- **Bullet**
- **DART**
- **Simbody**

These engines simulate:
- Rigid body motion  
- Collisions  
- Contact forces  
- Joint movements  

### Key Components
| Component | Meaning |
|----------|---------|
| **Gravity** | Pulls all objects downward. Default: `-9.81 m/s²`. |
| **Mass** | How heavy an object is. |
| **Inertia** | How difficult it is to rotate an object. |
| **Friction** | How surfaces resist motion. |
| **Bounce (Restitution)** | How much an object bounces after hitting something. |

---

## Collisions
Every object in Gazebo has a **collision mesh**.

- Used for physics calculations  
- More simple than the visual mesh  
- Determines how objects touch each other

**Example:**
A robot with wheels will have round collision meshes so surfaces interact correctly.

---

## Joints & Constraints
Robots move using **joints**, such as:
- Revolute (rotation)
- Prismatic (linear sliding)
- Continuous (360° rotation)
- Fixed (no movement)

Joint properties include:
- Limits  
- Motor forces  
- Velocity constraints  

---

## Why Accurate Physics Matters
A Digital Twin requires:
- True-to-life movement  
- Correct collisions  
- Realistic performance

This helps in:
- Robot testing  
- Predicting failures  
- Training AI movement models  
- Safe experimentation

---

## Summary
Physics simulation is the foundation of a Digital Twin.  
By accurately simulating gravity, collisions, and joint behavior, Gazebo helps you test real robots safely and efficiently.
