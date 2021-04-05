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
        self.actions = None # list of Action objects
        
class Utils():
    
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

class WorldObjects():
    def __init__(self, name):
        self.name = name
        self.family = None 

class Action():
    def __init__(self, name):
        self.name = name
        self. pre_cond = dict()
        self.effects = dict()
        
        
    
        