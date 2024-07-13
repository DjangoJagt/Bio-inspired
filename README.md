# Bio-inspired Reinforcement Learning Assignment

This repository contains the code and resources for the Bio-inspired Reinforcement Learning assignment. In this project, a reinforcement learning agent is trained to play the Asterix game, aiming to develop an efficient playing strategy.

## Overview

The agent was trained using Google Colab, with Google Drive employed to store logs and models for ease of reproducibility. For local execution, the code related to Colab and Google Drive has been commented out and modified for local environments. However, please note that running the code locally may lead to memory issues. It is advisable to download the necessary files and models to your local device and then upload them to Google Colab for training and testing.

## Configuration and Hyperparameter Tuning

The DQN model configuration is presented in the script, where hyperparameter tuning was performed by modifying the `config.update` parameters. The final parameters used are currently set, with the evaluated parameters commented out next to the values.

## Logs and Models

- **Training Logs**: The logs of each run are saved under specific `tb_log_names` to monitor the training process using TensorBoard.
- **Trained Models**: The trained models are saved in the `Saved_Models` directory. To further train or test a trained model, uncomment and use the appropriate saved model name.

The final extended run of 600,000 steps is saved as `Model_target_up_20k`.

## Testing Generalizability

To test the generalizability of the trained agent, the environment was changed to `SpaceInvadersNoFrameskip-v4` and `AssaultNoFrameskip-v4`.

## Instructions for Use

1. **Set Up the Environment**: Ensure you have all the necessary dependencies installed. It is recommended to use Google Colab for training and testing to avoid memory issues.
2. **Download and Upload Files**: Download the required files and models to your local device and upload them to Google Colab.
3. **Modify Configurations**: Update the `config.update` parameters as needed for your experiments.
4. **Monitor Training**: Use TensorBoard to monitor the training progress by checking the logs saved in `tb_log_names`.
5. **Load Trained Models**: To further train or test a trained model, uncomment the relevant saved model name in the script.

## Final Remarks

This repository provides the resources to train and test a reinforcement learning agent for the Asterix game and evaluate its generalizability to other games like Space Invaders and Assault. For any issues or further assistance, please refer to the comments in the code or reach out to the me Django Jagt.
