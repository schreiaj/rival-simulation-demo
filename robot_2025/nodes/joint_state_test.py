from tide import BaseNode
from robot_2025.models.joint import JointState
import math
import random

class JointStateTest(BaseNode):
    ROBOT_ID = "simbot"
    GROUP = "simulation"
    hz = 0.5

    def __init__(self, config=None):
        super().__init__(config=config)
        print("JointStateTest initialized")

    def step(self):
        joint_state = JointState(
            name=["fr_steering", "fl_steering", "rl_steering", "rr_steering"],
            # position=[math.radians(45.0), math.radians(135.0), math.radians(225.0), math.radians(315.0)],
            # generate random positions between -pi and pi
            position=[random.uniform(-math.pi, math.pi) for _ in range(4)],
            velocity=[1.0, 1.0, 1.0, 1.0],  # 1 rad/s for all steering joints
            effort=[]
        )

        self.put("cmd/joints", joint_state.to_bytes())
        