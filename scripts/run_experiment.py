import argparse
import torch

from maxent_irl_maps.experiment_management.parse_configs import setup_experiment
import pdb

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--setup_fp", type=str, required=True, help="path to the experiment yaml"
    )
    # add pretrained weight:
    parser.add_argument(
          "--pretrained_model", type=str, default=None,
          help="path to pretrained model weights (.pt file)"
      )
    args = parser.parse_args()
    res = setup_experiment(args.setup_fp)
    
    #load pretrained model:
    if args.pretrained_model is not None:
          print(f"Loading pretrained model from: {args.pretrained_model}")
          pretrained_dict = torch.load(args.pretrained_model, weights_only=True)

          # Get current model's state dict
          model_dict = res["algo"].network.state_dict()

          # Filter: only load weights with matching shapes
          matched_dict = {}
          skipped_keys = []
          #pdb.set_trace()
          for k, v in pretrained_dict.items():
              if k in model_dict:
                  if v.shape == model_dict[k].shape:
                      matched_dict[k] = v
                  else:
                      skipped_keys.append(f"{k}: pretrained {v.shape} vs current {model_dict[k].shape}")
              else:
                  skipped_keys.append(f"{k}: not in current model")

          # Load with strict=False to allow partial loading
          #pdb.set_trace()
          res["algo"].network.load_state_dict(matched_dict, strict=False)

          print(f"Pretrained model loaded successfully!")
          print(f"Matched layers: {len(matched_dict)}/{len(pretrained_dict)}")
          print(f"Skipped {len(skipped_keys)} layers due to shape mismatch")
          if len(skipped_keys) <= 10:
              for sk in skipped_keys:
                  print(f"    - {sk}")

    

    print("dataset size: {}".format(len(res["dataset"])))

    res["experiment"].run()
