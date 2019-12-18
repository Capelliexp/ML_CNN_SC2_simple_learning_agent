from customized_environments.envs.my_agent import CustomAgent

import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.policies import MlpLstmPolicy
from stable_baselines.common.policies import CnnPolicy
from stable_baselines.common.policies import CnnLstmPolicy

from stable_baselines.common.vec_env import DummyVecEnv, SubprocVecEnv

from stable_baselines import PPO2
from stable_baselines import ACKTR

from absl import flags

FLAGS = flags.FLAGS
FLAGS([''])

# create vectorized environment
env = DummyVecEnv([lambda: CustomAgent()])

model = ACKTR(
    CnnPolicy,
    env, 
    verbose=1, 
    tensorboard_log="gym_ouput/ACKTR_CNN/log/"
    )


model.setup_model()

for i in range(1,20):
    #save_name = "gym_ouput/ACKTR_CNN/it" + i.__str__()
    save_name = "gym_ouput/ACKTR_CNN/model"

    model.learn(total_timesteps=int(3e4), tb_log_name="ACKTR_CNN", reset_num_timesteps=False)
    model.save(save_name)
