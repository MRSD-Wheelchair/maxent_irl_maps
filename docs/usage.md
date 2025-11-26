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

Configuration files are located in the `config/` directory. You can take a look at `config/irl_wheelie.yaml` first for an example.

Example:
```bash
python3 run_experiment.py --setup_fp ../config/irl_wheelie.yaml
```

The model saving path is specified in the config file, for example
```yaml
experiment:
    save_to: /home/tartandriver/tartandriver_ws/workspace/experiments/irl
    name: irl_example
```

The model will be saved to `/home/tartandriver/tartandriver_ws/workspace/experiments/irl/<timestamp>-irl_example/`, and the log dir will look like:
```bash
tartandriver@PC:~/tartandriver_ws/workspace/experiments/irl/2025-11-26-01-48-23_irl_example$ tree
.
|-- _params.yaml
|-- dummy_dataset
|-- itr_1.pt
|-- itr_10.pt
|-- itr_2.pt
|-- itr_3.pt
|-- itr_4.pt
|-- itr_5.pt
|-- itr_6.pt
|-- itr_7.pt
|-- itr_8.pt
`-- itr_9.pt
```

## Evaluation

### Command

```bash
cd scripts
python3 run_eval.py --model_fp <path_to_model> --test_fp <path_to_test_data> --device cuda
```

example:
```bash
cd scripts

python3 run_eval.py \
--model_fp /home/tartandriver/tartandriver_ws/workspace/experiments/irl/2025-11-26-01-48-23_irl_example/itr_10.pt \
--test_fp /home/tartandriver/rosbags/irl_kitti_eval \
--device cuda
```

