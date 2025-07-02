> [!IMPORTANT]
> 🌟 Stay up to date at [opendrivelab.com](https://opendrivelab.com/#news)!

# Think Twice before Driving: Towards Scalable Decoders for End-to-End Autonomous Driving

- A SOTA Decoder for End-to-End Autonomous Driving under BEV
- [arXiv Paper](https://arxiv.org/abs/2305.06242) (CVPR 2023)

![pipeline](src/pipeline.PNG)
 
## Demo Video
[![Demo](src/demo_start.png)](https://youtu.be/ZhSH63O4Hsg)

## Getting Started

- [Installation](docs/INSTALL.md)
- [Closed-Loop Evaluation in Carla](docs/EVAL.md)
- [Prepare Dataset](docs/DATA_PREP.md)
- [Train Your Own Model](docs/TRAIN.md)
- [Calibrations for Different Camera Settings](camera_calibration/README.md) (Optional)

## Quick Run in Carla

Install the environment as in [Installation](docs/INSTALL.md), download our checkpoint ([GoogleDrive](https://drive.google.com/file/d/1Y2bWf8qVwqVQxqM2GOKTiR9kE9nGtkYV/view?usp=share_link) or [BaiduYun](https://pan.baidu.com/s/1OamwKOUpqK0EOqWa1Luv_g)(提取码 m5di).) (189K frames training set), put it into **open_loop_training/ckpt**, and run:

```shell
## In the ThinkTwice/ directory
CUDA_VISIBLE_DEVICES=0  nohup bash ./leaderboard/scripts/evaluation_town05long.sh 22023 22033 thinktwice_agent  False True open_loop_training/ckpt/thinktwice.pth+open_loop_training/configs/thinktwice.py all_towns_traffic_scenarios_no256 thinktwice_town05long 2>&1 > thinktwice_town05long.log &
```

Check [closed_loop_eval_log/eval_log](closed_loop_eval_log/eval_log) to see how our model drives in Carla! :oncoming_automobile:

(In case you have a screen to see the interface of Carla simulator, you could remove *DISPLAY=* in [leaderboard/leaderboard/leaderboard_evaluator.py](leaderboard/leaderboard/leaderboard_evaluator.py) and then you could directly watch with Carla.) 


## Code Structure

We give the structure of our code. Note that we only introduce those folders/files are commonly used and modified.

    ThinkTwice/
    ├── agents                  # From Carla official
    ├── camera_calibration      # When you want to use cameras with different FOV
    ├── closed_loop_eval_log    # Save eval logs
    ├── collect_data_json       # Save data collection logs
    ├── dataset                 # Data and metadata for training
    ├── leaderboard             # Code for Closed-Loop Evaluation
    │   ├── data                    # Save routes and scenarios
    │   ├── scripts                 # Run with Carla
    │   ├── team_code               # Your
    |   |   ├── roach_ap_agent_data_collection.py # Data collection
    │   |   └── thinktwice_agent.py      # Interface for closed-loop evaluation of our model
    │   ├── leaderboard             # From Carla official
    |   |   └── leaderboard_evaluator.py # Entrance of closed-loop evaluation
    ├── roach                   # Roach for data collection
    ├── scenario_runner         # From Carla official
    ├── open_loop_training      # Training and Neural Network
    |    ├── ckpt                    # Checkpoints
    |    ├── work_dirs               # Training Log
    |    ├── code                    # Preprocessing, DataLoader, Model
    |    │   ├── apis                    # Training pipeline for mmdet3D
    |    │   ├── core                    # The hooks for mmdet3D
    |    │   ├── datasets                # Preprocessing and DataLoader
    |    |   |   ├── pipelines                # Functions of Preprocessing and DataLoader
    |    │   |   ├── samplers                 # For DDP
    |    │   |   └── carla_dataset.py         # Framework of Preprocessing and DataLoading
    |    │   ├── model_code                   # Neural Network
    |    |   |   ├── backbones                # Module of Encoder
    |    |   |   └── dense_heads              # Module of Decoder and Loss Functions
    |    │   └── encoder_decoder_framework.py # Entrance of Neural Network
    |    └── train.py                # Entrance of Training

## License

All assets and code are under the [Apache 2.0 license](./LICENSE) unless specified otherwise.

## Bibtex
If this work is helpful for your research, please consider citing the following BibTeX entry.

```
@inproceedings{jia2023thinktwice,
  title={Think Twice before Driving: Towards Scalable Decoders for End-to-End Autonomous Driving},
  author={Jia, Xiaosong and Wu, Penghao and Chen, Li and Xie, Jiangwei and He, Conghui and Yan, Junchi and Li, Hongyang},
  booktitle={CVPR},
  year={2023}
}
```

## Related Resources
Many thanks to the open-source community!

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) 
- [End-to-end Autonomous Driving Survey](https://github.com/OpenDriveLab/End-to-end-Autonomous-Driving) (:rocket:Ours!)
- [TCP](https://github.com/OpenPerceptionX/TCP) (:rocket:Ours!)
- [BEVFormer](https://github.com/fundamentalvision/BEVFormer) (:rocket:Ours!)
- [UniAD](https://github.com/OpenDriveLab/UniAD) (:rocket:Ours!)
- [ST-P3](https://github.com/OpenPerceptionX/ST-P3) (:rocket:Ours!)
- [Carla](https://github.com/carla-simulator/carla)
- [Roach](https://github.com/zhejz/carla-roach)
- [Transfuser](https://github.com/autonomousvision/transfuser)
- [CARLA_GARGE](https://github.com/autonomousvision/carla_garage)
- [LAV](https://github.com/dotchen/LAV)
- [IBISCape](https://github.com/AbanobSoliman/IBISCape)
