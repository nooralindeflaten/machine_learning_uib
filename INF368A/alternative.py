import numpy as np
from matplotlib import pyplot
import gymnasium as gym
import bandit

env_1 = gym.make(bandit.Bandits_one(10))
#env_2 = gym.make(bandit.Bandits_two())
#env_3 = gym.make(bandit.Bandits_three())
#env_4 = gym.make(bandit.Bandits_four())
'''
class Agent():
    def __init__(self,k,mu,sigma):
        self.k = k
'''