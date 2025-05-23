import numpy as np
from collections import deque


from sklearn.metrics import roc_auc_score

from stable_baselines3 import PPO, SAC, DQN 

import os 
import glob 
import pickle
import json 
from datetime import datetime 

from environment_util import make_env 



import argparse 

from river import drift 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=str, default="cartpole", help="name of environment")
    parser.add_argument("--policy-type", type=str, default="dqn", help="type of rl policy")
    parser.add_argument("--model-type", type=str, default="single", help="type of drift detector models")
    parser.add_argument("--env0-steps", type=int, default=1000, help="Validation Steps")
    parser.add_argument("--env1-steps", type=int, default=3000, help="Undrifted Steps")
    parser.add_argument("--env2-steps", type=int, default=3000, help="Semantic Drift Steps")
    parser.add_argument("--env3-steps", type=int, default=3000, help="Noisy Drift Steps")
    parser.add_argument("--n-exp-per-model", type=int, default=10, 
                        help="number of experiments of each trained model.") 

    args = parser.parse_args() 

    allowed_envs = {"cartpole", "lunarlander", "hopper", 
                    "halfcheetah", "humanoid"}
    
    allowed_policy_types = {"dqn", "ppo", "sac"}
    
    if args.env not in allowed_envs:
        raise NotImplementedError(f"The environment {args.env} is not supported.")
    if args.policy_type not in allowed_policy_types:
        raise NotImplementedError(f"The policy {args.policy_type} is not supported.")

    print("Parsed arguments: ")
    print(args) 

    model_folder = os.path.join("trained_models", args.policy_type+'-'+args.env)
    if args.model_type == "single":
        pattern = "single_[0-9]"
    elif args.model_type == "single_noise":
        pattern = "single_noise_[0-9]"
    elif args.model_type == "single_drift":
        pattern = "single_drift_[0-9]"
    else:
        pattern = "ensemble_[0-9]"


    
    # Load Drift Detector Models
    loaded_models = []
    model_pattern = os.path.join(model_folder, pattern)
    print(model_pattern)
    matching_models = glob.glob(model_pattern)

    print(matching_models) 
    if len(matching_models)==0:
        raise NotImplementedError(f"There is no trained model for the environment {args.env}.")





if __name__ == "__main__":
    main()