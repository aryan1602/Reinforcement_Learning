import numpy as np

class GridWorld:
    def __init__(self, start_state=0, end_state=23, gamma=0.9, shape=(5, 5), obstacles=[11, 17], water=[21]):
        self.action = None
        self.start_state = start_state
        self.end_state = end_state
        self.shape = shape
        self.obstacles = obstacles
        self.water = water
        self.state = start_state
        self.reward = 0
        self.prob_stay = 0.1
        self.prob_rleft = 0.05
        self.prob_rright = 0.05
 
    def next_action(self, policy):
        prob = np.random.uniform()
        for i in range(len(policy[self.state])):
            if(prob < policy[self.state][i]):
                return i
            else:
                prob -= policy[self.state][i]
            
    def next_state(self):
        prob = np.random.uniform()
        if(prob < 0.05):
            self.action = (self.action + 3)%4
        elif(prob < 0.1):
            self.action = (self.action + 1)%4
        elif(prob < 0.2):
            self.action = None
        new_state = self.state
        if(self.action == None):
            return new_state
        
        if(self.action == 0):
            new_state -= 5
        elif(self.action == 1):
            new_state += 1
        elif(self.action == 2):
            new_state += 5
        else:
            new_state -= 1
        if(new_state < 0 or new_state > self.end_state or new_state in self.obstacles):
            new_state = self.state
        return new_state
    
    def get_reward(self):
        new_reward = 0
        if(self.state in self.water):
            new_reward = -10
        elif(self.state == self.end_state):
            new_reward = 10
        return new_reward
    
    def take_step(self, policy):
        self.action = self.next_action(policy)
        self.state = self.next_state()
        self.reward = self.get_reward()
        return self.state, self.reward
    
    def is_end_state(self):
        if self.state == self.end_state:
            return True
        else:
            return False

