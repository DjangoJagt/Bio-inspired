# Bio-inspired
This is the repository for the Bio-inspired reinforcements learning assignment.
In this assignment a reinforcement learning agent is trained to play the asterix game and learn a playing strategy as efficient as possible. 

This agent was trained in google colab using google drive to store logs and models for easy of reproducibility I commented the code related to colab and google drive and changed it to the local version however it will probably run into memory issues .  

Under the configuration DQN model the standard configuration is presented and this is also the part where hyperparameter tuning was performed by changing config.update. 

The logs of every run are saved under the specific tb_log_names to monitor the training process of every run in tensorboard. Furthermore the trained models are saved under the names of saved_models and to further train or test a trained model these models should be reloaded by uncommenting the correct saved_model name. 

The final extended run of 600,000 steps is the saved_model = "Model_target_up_20k" 
