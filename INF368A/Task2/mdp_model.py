import numpy as np
from typing import Tuple
import random

class Rover():
    def __init__(self):
        self.action = ["exploration", "pictures","sampling","recharging","malfunction"]
        self.actions = {
            "exploration": ["exploration","pictures","sampling","recharging"],
            "pictures": ["exploration", "sampling"],
            "sampling": ["exploration","recharging","sampling","malfunction"],
            "recharging": ["exploration"],
            "malfunction": []
        }
        
        return
        
    '''
    
    Enrich the previous Mars Rover scenario 
    with the following rewards: 0 for normal exploration, 
    +5 for taking pictures of the skies, 
    +20 for collecting samples from the ground, 
    0 for recharging, -100 for malfunctioning.
    '''
    # Get next state and reward based on current state and action
    def get_possible_actions(self,action:str):
        return self.actions[action]
    
    def get_reward(self,action):
        rewards = {
            "exploration": 0,
            "pictures": 5,
            "sampling": 20,
            "recharging": 0,
            "malfunction": -100}
        return rewards[action]
    
    def update_state(self,state,action):
        state = (state[1],action)
        reward = self.get_reward(action)
        return state,reward
    
    def get_next_action(self,current_action,action):
        if (current_action,action) == ("exploration","exploration"):
            return 0.7
        if (current_action,action) == ("exploration","pictures"):
            return 0.1
        if (current_action,action) == ("exploration","sampling"):
            return 0.1
        if (current_action,action) == ("exploration","recharging"):
            return 0.1
        if (current_action,action) == ("pictures","exploration"):
            return 0.6
        if (current_action,action) == ("pictures","sampling"):
            return 0.4
        if (current_action,action) == ("sampling","exploration"):
            return 0.35
        if (current_action,action) == ("sampling","recharging"):
            return 0.3
        if (current_action,action) == ("sampling","sampling"):
            return 0.3
        if (current_action,action) == ("sampling","malfunction"):
            return 0.05
        if (current_action,action) == ("recharging","exploration"):
            return 1.0
        
    def get_random_action(self,action_one):
        weights = [(self.get_next_action(action_one,x)) for x in self.actions[action_one]]
        action = np.random.choice(self.actions[action_one], 1, p=weights)
        return action[0]