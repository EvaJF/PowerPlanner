#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pddlpy import DomainProblem
from collections import defaultdict
import itertools

## Core classes ##

class Domain():
    
    def __init__(self, pddlpy_domprob):
        self.domprob = pddlpy_domprob
        self.current_state = None # State object
        self.goal_state_set = None # dic with caracteristics of goal (? rather than State object)
        self.action_dic = None # list of actions
        self.objects = None # list of world objects
        self.reversed_objects = None # for type of object, list of instances
        self.parser()
    
    def parser(self):
        world_dic = self.domprob.worldobjects()
        # object list
        obj_dic = dict()
        for obj in world_dic.keys():
            wo = WorldObject(name = obj)
            wo.family = world_dic[obj]
            obj_dic[obj] = wo
        
        # reversed objects
        self.reversed_objects = defaultdict(list)
        for obj,typ in self.domprob.problem.objects.items():
            self.reversed_objects[typ].append(obj)

        # action list
        action_dic = dict()
        for op in self.domprob.operators():
            my_op = Action(name = op)
            action_dic[op]=my_op
        for op in action_dic.keys():
            operator = self.domprob.domain.operators[op]
            var_names = operator.variable_list.keys()
            var_types = operator.variable_list.values()
            var_combinations = itertools.product(*[self.reversed_objects[typ] for typ in var_types])
            for var_list in var_combinations:
                value=dict()
                # ground preconditions and effects
                value["preconditions_pos"] = {prec.ground({name:inst for (name, inst) in zip(var_names, var_list)}) for prec in operator.precondition_pos}
                value["preconditions_neg"] =  {prec.ground({name:inst for (name, inst) in zip(var_names, var_list)}) for prec in operator.precondition_neg}
                value["effets_pos"] = {prec.ground({name:inst for (name, inst) in zip(var_names, var_list)}) for prec in operator.effect_pos}
                value["effets_neg"] = {prec.ground({name:inst for (name, inst) in zip(var_names, var_list)}) for prec in operator.effect_neg}
                action_dic[op].action_dic[tuple(var_list)] = value  


                init_state_set = set()


        init_state=self.domprob.initialstate()
        init_state_set = set()
        for i in range(len(init_state)):
            [carac, obj] = init_state.pop().__dict__["predicate"]
            init_state_set.add((carac, obj))
                

        # goal
        goal = self.domprob.goals()
        goal_state_set = set()
        for i in range(len(goal)):
            [carac, obj] = goal.pop().__dict__["predicate"]
            goal_state_set. add((carac, obj))
     
        ## Update ##
        self.current_state = State(true_predicates=init_state_set, goal_state = goal_state_set)
        self.goal_state_set = goal_state_set
        self.action_dic = action_dic
        self.objects = obj_dic
    
    
class State():
    def __init__(self, true_predicates, goal_state):
        self.state = true_predicates
        self.goal_state = goal_state
    
    def apply(self, action, arg_tuple):
        """
        DOESNT Directly modifies the State object by applying, if possible,
        the desired action with the given arg_tuple.
        If not possible, the State  object remains unchanged. 
        """
        #Check if the action is OK
        if not arg_tuple in action.action_dic.keys():
            return None
        
        action_specific = action.action_dic[arg_tuple]
        #Check les préconditions positives, si ok modifier l'état
        if self.state.issuperset(action_specific["preconditions_pos"]):
            newState = self.state.union(action_specific["effets_pos"]).difference(action_specific["effets_neg"])

            return newState
        else :
            return None

    def getChildren(self, actions):
        children=[]
        for action_name, action in actions.items() :
            for argTupple in list(action.action_dic.keys()):
                precondPos=action.action_dic[argTupple]["preconditions_pos"]
                precondNeg=action.action_dic[argTupple]["preconditions_neg"]
                if precondPos.issubset(self.state) and precondNeg.isdisjoint(self.state) :
                    stateAtteignable = self.apply(action, argTupple)
                    children.append((action_name, argTupple, State(true_predicates=stateAtteignable, goal_state=self.goal_state)))
        return children



    def update(self,action, arg_tuple):
        self.state = self.apply(action, arg_tuple)

    def isFinal(self):
        return self.goal_state.issubset(self.state)


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
        self.action_dic=dict()
        self.arg_type = list()
                        
        
 

if __name__ == '__main__': # for testing
    domainfile = "./domains/domain_recipies.pddl" 
    problemfile = "./domains/problems/pb_tartiflette.pddl" 
    domprob = DomainProblem(domainfile, problemfile)
    domain = Domain(pddlpy_domprob= domprob)