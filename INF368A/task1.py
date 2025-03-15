import numpy as np
from matplotlib import pyplot

#slot machine, prop R1(nothing) = 0.35, R2(5 dollars) = 0.3, R3(10 dollars) = 0.25, R4(20 dollars) = 0.1

#Plotting the distribution
def plot_slot(r,p):
    pyplot.bar(r,p)
    pyplot.xlabel('Price rewards in USD')
    pyplot.ylabel('P(R)')
    pyplot.show()

def e_and_var(rewards,probs):
    e = sum(rewards*probs)
    v = sum(pow(rewards-e,2) * probs)
    return e,v


#Distribution formula PMF or CDF
def prob_calc(rewards,probs):
    p_under_ten = sum((probs[:2]))
    print(p_under_ten)
    p_over_or_equal_ten = 1 - p_under_ten
    p_over_ten = 1 - sum(probs[:-1])
    return p_over_ten

def get_prob(rewards,probabilities,r):
    x = np.where(rewards==r)[0][0]
    return probabilities[x]
    
def prob_given(rewards,probs):
    # check for all combinations that can be less then 15, so which numbers in the array can be 15
    probabilities = []
    
    for i in rewards:
        for j in rewards:
            if i+j >= 15:
                probabilities.append(get_prob(rewards,probs,i)*get_prob(rewards,probs,j))
    return sum(probabilities)


r = np.array([0,5,10,20])
p = np.array([0.35,0.3,0.25,0.10])
print(prob_calc(r,p))


# Second slot machine
r1 = np.array([0,5,10,20])
p1 = np.array([0.3,0.35,0.3,0.05])
