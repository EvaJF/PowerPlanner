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
    
class Family():
    def __init__(self, name):
        self.name = "family"

class WorldObject():
    def __init__(self, name):
        self.name = name
        self.family = None 

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
obj_list = []
for obj in world_dic.keys():
    wo = WorldObject(name = obj)
    wo.family = world_dic[obj]
    obj_list.append(wo)
    print(wo)
print(obj_list)
    
# action list
action_list = []
for op in domprob.operators():
    print(op)
    my_op = Action(name = op)
    action_list.append(my_op)
    
# initial state
init_state = domprob.initialstate()
my_init_state = dict()
# there is going to be a name issue


# goal
        