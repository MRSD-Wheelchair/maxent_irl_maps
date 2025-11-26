# Setup Instructions

## Prerequisites

- Ubuntu 20.04 (Focal Fossa)
- [ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)
- Python 3.8+

## Dependencies

### ROS Packages

This package depends on the following ROS packages:

- `rclpy` (ROS 2 Client Library for Python) - *Note: The package.xml lists rclpy, but the README mentions ROS Noetic (ROS 1). Please verify if this is a hybrid or migration package.*
- `cv_bridge`
- `tf`
- `nav_msgs`
- `sensor_msgs`
- `geometry_msgs`
- `std_msgs`

### Python Dependencies

Install the required Python packages:

```bash
pip3 install torch torchvision torchaudio
pip3 install numpy matplotlib scipy pyyaml
```

### External Repositories

1. **rosbag_to_dataset**
   - Repository: [https://github.com/striest/rosbag_to_dataset](https://github.com/striest/rosbag_to_dataset)
   - Branch: `feature/irl_postproc`
   - Note: This dependency is primarily for generating new training data.

2. **torch_mpc**
   - Status: Private repository.
   - Contact: @striest for access.

## Installation

1. **Create a Workspace** (if you haven't already):
   ```bash
   mkdir -p ~/tartandriver_ws/src
   cd ~/tartandriver_ws/src
   ```

2. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   ```

3. **Install Dependencies**:
   ```bash
   cd ~/tartandriver_ws
   rosdep install --from-paths src --ignore-src -r -y
   ```

4. **Build the Package**:
   ```bash
   colcon build --symlink-install --packages-select maxent_irl_maps
   ```
   *Note: If using catkin (ROS 1), use `catkin_make` or `catkin build` instead.*

5. **Source the Workspace**:
   ```bash
   source install/setup.bash
   ```
