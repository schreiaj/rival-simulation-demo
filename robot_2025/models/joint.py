"""
Joint state models for robot control
"""

from typing import Dict, List, Optional
from pydantic import  Field
from tide.models import TideMessage

class JointState(TideMessage):
    """Represents the state of robot joints."""
    name: List[str]
    position: List[float]
    velocity: List[float]
    effort: List[float]
