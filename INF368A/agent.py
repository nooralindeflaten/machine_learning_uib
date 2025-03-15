import numpy as np

class Agent:
    def __init__(self, k, algorithm, args):
        self.k = k
        self.algorithm = algorithm
        self.args = args
        self.Q_vals = np.zeros(k)
        self.count = np.zeros(k)
    
    def select_action(self):
        return self.algorithm(self.Q_vals,self.count, **self.args)
    
    def update(self, action, reward):
     # Update the estimated rewards and counts
        self.count[action] += 1
        self.Q_vals[action] += (reward - self.Q_vals[action]) / self.count[action]

