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
    def parser(pddlpy_domprob):
        pass
    def heuristicSearch():
        pass
    
class State(Domain):
    
    def __init__(self):
        self.current_state = self.init_state
    
    def apply(self, action, arg_list):
        pass
    
    def update(self, action, arg_list):
        # if apply method does not return None, then set current state to new state
        pass
    

class WorldObject():
    def __init__(self, name):
        self.name = name
        self.family = "family"

class Action():
    def __init__(self, name):
        self.name = name
        self. pre_cond = dict()
        self.effects = dict()
        self.arg_type = list()
        
        
## Parsing  - DRAFT ##
        
world_dic = domprob.worldobjects()
print(world_dic)

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
    print(op)
    my_op = Action(name = op)
    action_dic[op]=my_op
print(action_dic)
    
# initial state
init_state = domprob.initialstate()

init_state_dic = dict()
for i in range(len(init_state)):
    [carac, obj] = init_state.pop().__dict__["predicate"]
    if obj in init_state_dic.keys():
        init_state_dic[obj][carac]=True
    else:
        init_state_dic[obj]=dict()
        init_state_dic[obj][carac]=True
        
print(init_state_dic)

# goal
goal = domprob.goals()
goal_state_dic = dict()
for i in range(len(goal)):
    [carac, obj] = goal.pop().__dict__["predicate"]
    if obj in goal_state_dic.keys():
        goal_state_dic[obj][carac]=True
    else:
        goal_state_dic[obj]=dict()
        goal_state_dic[obj][carac]=True
print(goal_state_dic)

# preconditions
        