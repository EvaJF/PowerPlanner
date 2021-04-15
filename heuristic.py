from abc import ABC, abstractmethod
import numpy as np

def heuristic_null(s):
    return 1

def heuristic_0(s):
    """returns the number of predicates that must be true in goal state but aren't """
    state = s.state
    pos_goal = s.pos_goal_state
    neg_goal = s.neg_goal_state
    # nb predicates that must be true but aren't + nb predicates that muse be false but aren't
    heur = len(pos_goal - state) + len(neg_goal.intersection(state))
    return heur

class Heuristic_HSP():
    
    def __init__(self, domain):
        self.domain = domain
        self.actions = domain.action_dic
        self.values = {}

    def heuristic_hsp(self, s):
        """Returns heuristic value in state s"""
        state = s.state
        pos_goal = s.pos_goal_state
        neg_goal = s.neg_goal_state
        heu_value = self.g_state_plus_hsp(state, pos_goal, explored=[], alpha=np.inf)  ## How to deal with neg_goal?
        self.values = {}
        return heu_value

    def g_state_plus_hsp(self, state, pos_goal, explored, alpha):
        """Computes the sum of heuristic values for each litteral of the goal"""
        g_value = 0
        for goal in pos_goal:
            if g_value > alpha:
                break
            if goal in self.values.keys():
                g_value += self.values[goal]
            else:
                g_value += self.g_litteral_hsp(state, goal, explored)
        return g_value
    
    def g_state_max_hsp(self, state, pos_goal, explored):
        """Computes the max of heuristic values among each litteral of the goal"""
        max_g_value = 0
        for goal in pos_goal:
            if goal in self.values.keys():
                g_value = self.values[goal]
            else:
                g_value = self.g_litteral_hsp(state, goal, explored)
            if g_value > max_g_value:
                max_g_value = g_value
        return max_g_value

    def g_litteral_hsp(self, state, goal, explored):
        """Compute capacity to reach litteral goal from state"""
        if goal in state:
            return 0
        else:
            min_value = np.inf
            for action_name, action in self.actions.items():   ## List of ground actions
                for argTupple in list(action.action_dic.keys()):    ## List of actual actions (with variables)
                    if goal in action.action_dic[argTupple]["effets_pos"]:
                        precondPos = action.action_dic[argTupple]["preconditions_pos"]
                        if precondPos not in explored:
                            new_value = 1 + self.g_state_plus_hsp(state, precondPos, 
                                                                  explored + [precondPos], alpha = min_value - 1)
                            self.values[goal] = new_value
                            if new_value < min_value:
                                min_value = new_value                    
        return min_value

class Heuristic_HSP_Neg():
    
    def __init__(self, domain):
        self.domain = domain
        self.actions = domain.action_dic
        self.values_pos = {}
        self.values_neg = {}

    def heuristic_hsp(self, s):
        """Returns heuristic value in state s"""
        state = s.state
        pos_goal = s.pos_goal_state
        neg_goal = s.neg_goal_state
        heu_value = self.g_state_plus_hsp(state, pos_goal, neg_goal, explored=[])  
        self.values_pos = {}
        self.values_neg = {}
        return heu_value

    def g_state_plus_hsp(self, state, pos_goal, neg_goal, explored):
        """Computes the sum of heuristic values for each litteral of the goal"""
        g_value = 0
        for goal in pos_goal:
            if goal in self.values_pos.keys():
                g_value += self.values_pos[goal]
            else:
                g_value += self.g_litteral_pos_hsp(state, goal, explored)
        for goal in neg_goal:
            if goal in self.values_neg.keys():
                g_value += self.values_neg[goal]
            else:
                g_value += self.g_litteral_neg_hsp(state, goal, explored)        
        return g_value


    def g_litteral_hsp(self, state, goal, explored):
        """Compute capacity to reach litteral goal from state"""
        if goal in state:
            return 0
        else:
            min_value = np.inf
            for action_name, action in self.actions.items():   ## List of ground actions
                for argTupple in list(action.action_dic.keys()):    ## List of actual actions (with variables)
                    if goal in action.action_dic[argTupple]["effets_pos"]:
                        precondPos = action.action_dic[argTupple]["preconditions_pos"]
                        if precondPos not in explored:
                            new_value = 1 + self.g_state_plus_hsp(state, precondPos, 
                                                                  explored + [precondPos], alpha = min_value - 1)
                            self.values[goal] = new_value
                            if new_value < min_value:
                                min_value = new_value                    
        return min_value    
    
    
    def g_litteral_pos_hsp(self, state, goal, explored):
        """Compute capacity to reach positive litteral goal from state"""
        if goal in state:
            return 0
        else:
            min_value = np.inf
            for action_name, action in self.actions.items():   ## List of ground actions
                for argTupple in list(action.action_dic.keys()):    ## List of actual actions (with variables)
                    if goal in action.action_dic[argTupple]["effets_pos"]:
                        precondPos = action.action_dic[argTupple]["preconditions_pos"]
                        precondNeg = action.action_dic[argTupple]["preconditions_neg"]
                        if precondPos not in explored:
                            new_value = 1 + self.g_state_plus_hsp(state, precondPos, precondNeg,
                                                                  explored + [precondPos])
                            self.values_pos[goal] = new_value
                            if new_value < min_value:
                                min_value = new_value                    
        return min_value
    
    def g_litteral_neg_hsp(self, state, goal, explored):
        """Compute capacity to reach negative litteral goal from state"""
        if goal not in state:
            return 0
        else:

            min_value = np.inf
            for action_name, action in self.actions.items():   ## List of ground actions
                for argTupple in list(action.action_dic.keys()):    ## List of actual actions (with variables)
                    if goal in action.action_dic[argTupple]["effets_neg"]:
                        precondPos = action.action_dic[argTupple]["preconditions_pos"]
                        precondNeg = action.action_dic[argTupple]["preconditions_neg"]
                        if precondPos not in explored:
                            new_value = 1 + self.g_state_plus_hsp(state, precondPos, precondNeg,
                                                                  explored + [precondPos])
                            self.values_neg[goal] = new_value
                            if new_value < min_value:
                                min_value = new_value 
        return min_value