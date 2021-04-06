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
        self.goal_state = None # State object
        self.actions = None # list of actions
        self.objects = None # list of world objects
        
    
        
class Utils():
    def parser(self,pddlpy_domprob):
        pass
    def heuristicSearch(self):
        pass
    
class State():
    def __init__(self, init_state):
        self.state = init_state
    
    def apply(self, action, arg_tupple):
        #Check if the action is OK
        if not arg_tupple in action.actions.keys():
            print("You can't perform this action with these arguments")
            return
        
        action_specific = action.actions[arg_tupple]
        #Check les préconditions positives
        if self.state.issuperset(action_specific["preconditions_pos"]):
            self.state = self.state.union(action_specific["effets_pos"]).difference(action_specific["effets_neg"])
            print("The state has been modified")
            print(self.state)
        
        else :
            print("The preconditions have not been met to perform this action")


    
    def update(self, action, arg_tupple):
        # if apply method does not return None, then set current state to new state
        pass
    

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

family_dic = dict()

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
        
state = State(init_state=init_state_set)
print(init_state_set)

# goal
goal = domprob.goals()
goal_state_set = set()
for i in range(len(goal)):
    [carac, obj] = goal.pop().__dict__["predicate"]
    goal_state_set. add((carac, obj))
print(goal_state_set)

        