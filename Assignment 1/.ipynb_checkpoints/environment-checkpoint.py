import numpy as np

class GridWorld:
    def __init__(self, start_state=0, end_state=23, gamma=0.9 shape=(5, 5), obstacles=[11, 17], water=[21]):
        self.start_state = start_state
        self.end_state = end_state
        self.shape = shape
        self.obstacles = obstacles
        self.water = water
        self.state = start_state
        self.reward = 0
        self.prob_stay = 0.1
        self.prob_rleft = 0.05
        self.prob.rright = 0.05
    
    def next_state(self, state, action):
        prob = np.random.uniform()
        if(prob < 0.05):
            action = (action + 3)%4
        elif(prob < 0.1):
            action = (action + 1)%4
        elif(prob < 0.2):
            action = None
        new_state = state
        if(action == None):
            return new_state
        
        if(action == 0):
            new_state -= 5
        else if(action == 1):
            new_state += 1
        else if(action == 2):
            new_state += 5
        else:
            new_state -= 1
        if(new_state < 0 or new_state > end_state or new_state in obstacles):
            new_state = state
        
        return new_state
    
    def get_reward(self, state):
        reward = 0
        if(state in water):
            reward = -10
        elif(state == end_state):
            reward = 10
        return reward
    
    def take_step(self, action):
        new_state = next_state(self.state, action)
        self.state = new_state
        reward = get_reward(new_state)
        return self.state, reward