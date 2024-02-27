import numpy as np

class GridWorld:
    def __init__(self, start_state=0, end_state=24, gamma=0.9, shape=(5, 5), obstacles=[11, 17], water=[21]):
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
        self.gamma = gamma
 
    def next_action(self, policy):
        return np.random.choice([0, 1, 2, 3], p=policy[self.state])

    def next_state(self, current_state, act):
        prob = np.random.uniform()
        if(prob < 0.05):
            act = (act + 3)%4
        elif(prob < 0.1):
            act = (act + 1)%4
        elif(prob < 0.2):
            act = None
        new_state = current_state
        if(act == None):
            return new_state
        
        if(act == 0):
            new_state -= 5
        elif(act == 1):
            if(new_state%5 != 4):
                new_state += 1
        elif(act == 2):
            new_state += 5
        else:
            if(new_state%5 != 0):
                new_state -= 1
        if(new_state < 0 or new_state > self.end_state or new_state in self.obstacles):
            new_state = current_state
        return new_state
    
    def get_reward(self, current_state):
        new_reward = 0
        if(current_state in self.water):
            new_reward = -10
        elif(current_state == self.end_state):
            new_reward = 10
          
        return new_reward
    
    def take_step(self, policy):
        self.action = self.next_action(policy)
        self.state = self.next_state(self.state, self.action)
        self.reward = self.get_reward(self.state)
        return self.state, self.reward
    
    def is_end_state(self):
        if self.state == self.end_state:
            return True
        else:
            return False

