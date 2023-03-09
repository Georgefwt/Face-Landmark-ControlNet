import torch
import argparse

def prune_ckpt(ckpt_path, save_path):
    raw = torch.load(ckpt_path, map_location=torch.device('cpu'))
    state_dict = raw["state_dict"]
    torch.save(state_dict, save_path)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--ckpt_path', type=str)
    args.add_argument('--save_path', type=str)
    args = args.parse_args()
