# Architecture Overview

## Directory Structure

```
maxent_irl_maps/
├── config/                 # Configuration files for experiments and training
├── docs/                   # Documentation
├── launch/                 # ROS launch files
├── scripts/                # Executable scripts for training, evaluation, and ROS nodes
├── src/
│   └── maxent_irl_maps/    # Python package source code
│       ├── algos/          # IRL algorithms (e.g., MPPI IRL)
│       ├── dataset/        # Dataset handling and loading
│       ├── experiment_management/ # Experiment setup and parsing
│       ├── metrics/        # Evaluation metrics
│       ├── networks/       # Neural network architectures
│       └── utils.py        # Utility functions
├── package.xml             # ROS package definition
├── setup.py                # Python package setup
└── README.md               # Main entry point
```

## Key Components

### Algorithms (`src/maxent_irl_maps/algos/`)
Contains the core Inverse Reinforcement Learning algorithms.
- `mppi_irl_speedmaps.py`: Main IRL training code using Model Predictive Path Integral (MPPI) control.

### Experiment Management (`src/maxent_irl_maps/experiment_management/`)
Handles configuration and experiment setup.
- `parse_configs.py`: Registry mapping strings to files for setting up experiments. New network definitions should be registered here.

### Scripts (`scripts/`)
- `run_experiment.py`: Entry point for training models.
- `generate_metrics.py`: Evaluates trained models.
- `ros/gridmap_to_cvar_costmap.py`: ROS node for deploying the trained model.

## Data Flow

1. **Input**: Rosbags containing GridMaps, Odometry, Images, and Steering Angle.
2. **Preprocessing**: `rosbag_to_dataset` converts rosbags to a dataset format. `preprocess_dataset_no_pointpillars.py` further processes it for IRL.
3. **Training**: `run_experiment.py` uses the processed data to train the IRL network.
4. **Output**: Trained network weights saved in the experiment directory.
5. **Deployment**: The trained network is loaded by the ROS node to generate costmaps for navigation.
