import os
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy


environment_name = 'CartPole-v1'
env = gym.make(environment_name, render_mode="human")

episodes = 5
for episode in range(1,episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, terminated, truncated, info = env.step(action)
        score += reward

        done = terminated or truncated
    print('episode:{} Score:{}'.format(episode, score))
env.close

# def test_car_racing():
#     env = gym.make('CarRacing-v2', render_mode="human")  # Make sure you use the correct environment name
#     env.reset()
#     for _ in range(1000):
#         env.render()
#         action = env.action_space.sample()  # Take a random action
#         observation, reward, terminated, truncated, info = env.step(action)
#         if terminated or truncated:
#             observation, info = env.reset()

#     env.close()

# if __name__ == "__main__":
#     test_car_racing()
