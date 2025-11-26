# maxent_irl_maps

Code for running MaxEnt IRL for offroad navigation.

## Documentation

- [**Setup Guide**](docs/setup.md): Installation instructions and dependencies.
- [**Usage Guide**](docs/usage.md): How to run experiments, generate metrics, and use ROS nodes.
- [**Architecture Overview**](docs/architecture.md): Explanation of the codebase structure and key components.

## Overview

This code is designed to train a network for inverse RL for a ROS-based autonomy stack similar to [TartanDrive](https://github.com/castacks/tartan_drive_2.0). At a high level, its input is rosbags with the following:

1. [GridMaps](https://github.com/ANYbotics/grid_map) of local terrain
2. [Odometry](http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html) of robot state
3. [Images](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Image.html) FPV images (viz only for now)
4. Steering Angle (as stamped Float32 in deg, robot specific)

Note that we require both grid maps and odometry to be in the same frame.

Outputs will be a directory of trained networks that can be run on robot with the ROS script.

## Quick Start

1. **Install dependencies**: See [Setup Guide](docs/setup.md).
2. **Run an experiment**:
   ```bash
   cd scripts
   python3 run_experiment.py --setup_fp ../config/training/pointpillars_debug.yaml
   ```