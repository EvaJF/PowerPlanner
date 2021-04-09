#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:18:53 2021

@author: eva
"""

from pddlpy import DomainProblem

# for testing
domainfile = "./domains/domain_recipies.pddl" 
problemfile = "./domains/problems/pb_tartiflette.pddl" 
domprob = DomainProblem(domainfile, problemfile)


## Core classes ##

class Domain():
    
    def __init__(self, pddlpy_domprob):
        self.domprob = pddlpy_domprob
        self.init_state = None # State object
        self.goal_state_set = None # dic with caracteristics of goal (? rather than State object)
        self.actions = None # list of actions
        self.objects = None # list of world objects
    
    def parser(self, pddlpy_domprob):
        world_dic = pddlpy_domprob.worldobjects()
        # object list
        obj_dic = dict()
        for obj in world_dic.keys():
            wo = WorldObject(name = obj)
            wo.family = world_dic[obj]
            obj_dic[obj] = wo   
        print(obj_dic)
        # action list
        action_dic = dict()
        for op in domprob.operators():
            my_op = Action(name = op)
            action_dic[op]=my_op
        for op in action_dic.keys():
            L=list(domprob.ground_operator(op))
            for i in range(len(L)):
                tupleComnbi = tuple(list(L[i].variable_list.values()))
                value=dict()
                value["preconditions_pos"]=L[i].precondition_pos
                value["preconditions_neg"]=L[i].precondition_neg
                value["effets_pos"]=L[i].effect_pos
                value["effets_neg"]=L[i].effect_neg
                action_dic[op].actions[tupleComnbi]=value
        print(action_dic)            
        # initial state
        init_state = pddlpy_domprob.initialstate()        
        init_state_set = set()
        for i in range(len(init_state)):
            [carac, obj] = init_state.pop().__dict__["predicate"]
            init_state_set.add((carac, obj))                
        print(init_state_set)
        # goal
        goal = domprob.goals()
        goal_state_set = set()
        for i in range(len(goal)):
            [carac, obj] = goal.pop().__dict__["predicate"]
            goal_state_set. add((carac, obj))
        print(goal_state_set)
        ## Update ##
        self.init_state = State(true_predicates=init_state_set)
        self.goal_state_set = goal_state_set
        self.actions = action_dic
        self.objects = obj_dic
    
    
class State():
    def __init__(self, true_predicates):
        self.state = true_predicates
    
    def apply(self, action, arg_tuple):
        """
        Directly modifies the State object by applying, if possible,
        the desired action with the given arg_tuple.
        If not possible, the State  object remains unchanged. 
        """
        #Check if the action is OK
        if not arg_tuple in action.actions.keys():
            print("You can't perform this action with these arguments.")
            return None
        
        action_specific = action.actions[arg_tuple]
        #Check les préconditions positives, si ok modifier l'état
        if self.state.issuperset(action_specific["preconditions_pos"]):
            self.state = self.state.union(action_specific["effets_pos"]).difference(action_specific["effets_neg"])
            print("The state was modified.")
            print(self.state)        
        else :
            print("The preconditions for performing this action have not been met.")
        return None

    def heuristic1(self, goal_state_set):
        n_diff = len(self.state.difference(goal_state_set)) + len(goal_state_set.difference(self.state))
        return n_diff
    

class WorldObject():
    def __init__(self, name):
        self.name = name
        self.family = "family"


class Action():
    def __init__(self, name):
        self.name = name
        self.actions=dict()
        self.arg_type = list()
                        
        
 

    
    
## Parsing  - DRAFT ##
        
world_dic = domprob.worldobjects()


# object list
obj_dic = dict()

for obj in world_dic.keys():
    wo = WorldObject(name = obj)
    wo.family = world_dic[obj]
    obj_dic[obj] = wo
    
print(obj_dic)
    
# action list
action_dic = dict()
for op in domprob.operators():
    my_op = Action(name = op)
    action_dic[op]=my_op

for op in action_dic.keys():
    L=list(domprob.ground_operator(op))
    for i in range(len(L)):
        tupleComnbi = tuple(list(L[i].variable_list.values()))
        value=dict()
        value["preconditions_pos"]=L[i].precondition_pos
        value["preconditions_neg"]=L[i].precondition_neg
        value["effets_pos"]=L[i].effect_pos
        value["effets_neg"]=L[i].effect_neg
        action_dic[op].actions[tupleComnbi]=value

    
# initial state
init_state = domprob.initialstate()

init_state_set = set()
for i in range(len(init_state)):
    [carac, obj] = init_state.pop().__dict__["predicate"]
    init_state_set.add((carac, obj))
        
state = State(true_predicates=init_state_set)
print(init_state_set)

# goal
goal = domprob.goals()
goal_state_set = set()
for i in range(len(goal)):
    [carac, obj] = goal.pop().__dict__["predicate"]
    goal_state_set. add((carac, obj))
print(goal_state_set)

# test heuristic 0 
h0 = len(init_state_set.difference(goal_state_set)) + len(goal_state_set.difference(init_state_set))
print(h0)

print(init_state_set.difference(goal_state_set))
print(goal_state_set.difference(init_state_set))

# test heuristic 1
h1 = max(len(init_state_set.difference(goal_state_set)), len(goal_state_set.difference(init_state_set)))
print(h1)


        