# Python Agents with rclpy

To build intelligent robots, we need two things:

1. **ROS 2** for real-time control  
2. **Python AI agents** for decision-making  

With `rclpy`, we can bridge AI logic to ROS controllers.

---

## 🤖 What Is an AI Agent?

An **AI agent** is a program that:
- Observes the environment  
- Decides an action  
- Sends command to the robot  

Example:
- Vision agent processes camera frames  
- Planning agent decides where to move  
- Voice assistant agent listens and responds  

---

## 🔗 Why Use Agents With ROS 2?

AI agents need to:
- Subscribe to robot sensors  
- Publish control commands  
- Call services (e.g., "stop robot")  
- Listen to feedback via actions  

`rclpy` provides all tools needed.

---

## 🐍 Creating an Agent Node in Python

Here is a basic skeleton:

```python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DecisionAgent(Node):
    def __init__(self):
        super().__init__("decision_agent")

        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.get_logger().info("Agent ready")

    def move_forward(self):
        msg = Twist()
        msg.linear.x = 0.2
        self.publisher.publish(msg)


from sensor_msgs.msg import LaserScan

self.create_subscription(
    LaserScan,
    "/scan",
    self.laser_callback,
    10
)

def laser_callback(self, msg):
    if min(msg.ranges) < 0.5:
        self.stop()
