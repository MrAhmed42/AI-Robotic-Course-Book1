# Nodes, Topics, and Services in ROS 2

ROS 2 provides the communication backbone for modern robots. To understand how a robot "thinks," "talks," and "responds," we must understand three core concepts:

- **Nodes**  
- **Topics**  
- **Services**

Together, they form the nervous system of a robot.

---

## 🚀 What Are ROS 2 Nodes?

A **node** is a small program that performs one specific task.

Examples of nodes:
- A camera node that publishes images  
- A motor controller node that moves wheels  
- A SLAM node that builds a map  
- A voice command node that listens to speech  

### 🧩 Why nodes?

Nodes make robot software:
- **Modular**  
- **Easy to debug**  
- **Reusable**  
- **Distributed** (can run on multiple computers)

### Creating Nodes
Nodes can be written in:
- **Python (`rclpy`)**
- **C++ (`rclcpp`)**

Example Python node:

```python
import rclpy
from rclpy.node import Node

class SimpleNode(Node):
    def __init__(self):
        super().__init__("simple_node")
        self.get_logger().info("Node started")

rclpy.init()
rclpy.spin(SimpleNode())
rclpy.shutdown()
