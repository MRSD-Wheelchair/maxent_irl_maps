# Usage Guide

## Attach to docker container

```bash
cd /home/thomaschan/mrsd_wheelchair/tartandriver_ws-IRL
./run/attach_docker
cd /home/tartandriver/tartandriver_ws/src/planning/maxent_irl_maps/
```

## Running Experiments

The main driver script for running experiments is `scripts/run_experiment.py`.

### Command

```bash
cd scripts
python3 run_experiment.py --setup_fp <path_to_config>
```

### Configuration

Configuration files are located in the `config/` directory. A good starting point for debugging is `config/training/pointpillars_debug.yaml`.

Example:
```bash
python3 run_experiment.py --setup_fp ../config/irl_wheelie.yaml
```

## Evaluation

### Command

```bash
cd scripts
python3 run_eval.py --model_fp <path_to_model> --test_fp <path_to_test_data> --device cuda
```
