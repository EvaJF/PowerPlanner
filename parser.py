#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pddlpy import DomainProblem

# for testing
domainfile = "./domains/domain_recipies.pddl" 
problemfile = "./domains/problems/pb_tartiflette.pddl" 
domprob = DomainProblem(domainfile, problemfile)


## Core classes ##

class Domain():
    
    def __init__(self, pddlpy_domprob):
        self.domprob = pddlpy_domprob
        self.current_state = None # State object
        self.goal_state_set = None # dic with caracteristics of goal (? rather than State object)
        self.action_dic = None # list of actions
        self.objects = None # list of world objects
        self.parser()
    
    def parser(self):
        world_dic = self.domprob.worldobjects()
        # object list
        obj_dic = dict()
        for obj in world_dic.keys():
            wo = WorldObject(name = obj)
            wo.family = world_dic[obj]
            obj_dic[obj] = wo   

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
                action_dic[op].action_dic[tupleComnbi]=value  


                init_state_set = set()


        init_state=self.domprob.initialstate()
        init_state_set = set()
        for i in range(len(init_state)):
            [carac, obj] = init_state.pop().__dict__["predicate"]
            init_state_set.add((carac, obj))
                

        # goal
        goal = domprob.goals()
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
            #print("You can't perform this action with these arguments.")
            return None
        
        action_specific = action.action_dic[arg_tuple]
        #Check les préconditions positives, si ok modifier l'état
        if self.state.issuperset(action_specific["preconditions_pos"]):
            newState = self.state.union(action_specific["effets_pos"]).difference(action_specific["effets_neg"])
            #print("The state was modified.")
            #print(self.state)
            return newState
        else :
            #print("The preconditions for performing this action have not been met.")
            return None

    def getChildren(self, actions):
        children=[]
        for action in actions.keys() :
            #print(action)
            #print(list(actions[action].action_dic.keys()))
            for argTupple in list(actions[action].action_dic.keys()):
                print(actions[action].action_dic[argTupple])
                precondPos=actions[action].action_dic[argTupple]["preconditions_pos"]
                precondNeg=actions[action].action_dic[argTupple]["preconditions_neg"]
                if precondPos.issubset(self.state) and precondNeg.isdisjoint(self.state) :
                    print(action, argTupple)
                    stateAtteignable = self.apply(actions[action], argTupple)
                    children.append((action, argTupple, stateAtteignable))
        return children



    def update(self,action, arg_tuple):
        self.state = self.apply(action, arg_tuple)

    def isFinal(self):
        return self.goal_state.issubset(self.state)


    

class WorldObject():
    def __init__(self, name):
        self.name = name
        self.family = "family"


class Action():
    def __init__(self, name):
        self.name = name
        self.action_dic=dict()
        self.arg_type = list()
                        
        
class Utils():
        
    def heuristicSearch(self):
        pass
    

domain = Domain(pddlpy_domprob= domprob)
