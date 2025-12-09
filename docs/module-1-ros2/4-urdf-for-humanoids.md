# URDF for Humanoids

A robot’s physical structure must be described in a standardized format so ROS can understand it.  
This is where **URDF (Unified Robot Description Format)** comes in.

URDF describes:
- Links (body parts)
- Joints (how parts move)
- Inertial properties
- Sensors & actuators
- Collision models
- Visual meshes

---

## 🦾 Why URDF Matters for Humanoid Robots

Humanoids are complex because they have:

- Multiple limbs  
- Many DOF joints  
- Balance requirements  
- Sensors on head and hands  
- Control loops that depend on kinematics  

URDF provides the **digital blueprint** of the robot.

---

## 🧩 URDF Structure

A humanoid URDF contains:

robot
├── base_link
├── torso
├── head
├── left_arm
├── right_arm
├── left_leg
└── right_leg


Each consists of:
- `link` → rigid body  
- `joint` → mechanism connecting links  

---

## ⚙️ Example: A Basic Leg Joint

```xml
<link name="upper_leg">
  <inertial>
    <mass value="3.0"/>
    <origin xyz="0 0 0"/>
  </inertial>
</link>

<joint name="knee_joint" type="revolute">
  <parent link="upper_leg"/>
  <child link="lower_leg"/>
  <origin xyz="0 0 -0.3"/>
  <axis xyz="0 1 0"/>
  <limit effort="50" velocity="1.5" lower="0" upper="2.5"/>
</joint>
