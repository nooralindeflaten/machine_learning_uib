import numpy as np

def epsilon_greedy(Q_vals, count,episode,epsilon):
    # Implementation
    if np.random.rand() < epsilon:
        return np.random.choice(len(Q_vals))
    return np.argmax(Q_vals)
    
def decaying_epsilon_greedy(Q_vals, count,episode, episodes, init_epsilon,min_epsilon=0.01):
    rate = (init_epsilon - min_epsilon) / episodes
    epsilon = max(init_epsilon - rate * episode, min_epsilon)
    return epsilon_greedy(Q_vals,count,episode,epsilon)

def ucb(Q_vals, count, episode,c=2):
    total_counts = np.sum(count)
    ucb_values = Q_vals + c * np.sqrt(np.log(total_counts + 1) / (count + 1e-5))
    return np.argmax(ucb_values)

