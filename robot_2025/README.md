# 2025 Robot Simulation

A Tide-based robotics project that provides a PyBullet simulation environment for robot control and testing.

## Features

- Real-time robot simulation using PyBullet
- Joint state control and monitoring
- Configurable simulation parameters
- URDF-based robot model support
- Real-time physics simulation at 240Hz
- Joint position, velocity, and effort control

## Getting Started

Run the simulation:

```bash
uv run tide up
```

Or run directly with:

```bash
uv run  main.py
```

## Project Structure

- `nodes/`: Contains the simulation node implementations
  - `sim.py`: Main simulation node that handles PyBullet integration
  - `joint_state_test.py`: Test node for joint state control
- `models/`: Data models for robot state and control
- `assets/`: Contains robot URDF files and other assets
- `config/`: Configuration files for node setup
- `main.py`: Project entry point

## Simulation Node

The main `SimulationNode` provides:

1. Real-time physics simulation using PyBullet
2. Joint state control through Tide topics
3. Configurable simulation parameters:
   - Simulation rate (default: 240Hz)
   - Headless mode option
   - Custom URDF path support
   - Robot ID configuration

## Configuration

The simulation can be configured through `config/config.yaml`. Key parameters include:

- `robot_id`: Identifier for the robot
- `headless`: Run simulation without GUI (not implemented)
- `sim_rate`: Physics simulation rate
- `urdf_path`: Path to robot URDF file

## Next Steps

1. Add in web based driver station
2. Add in dashboard system
3. Implement proper kinematics
4. Import field model into simulation

Refer to the Tide documentation for more information about node development and configuration. 