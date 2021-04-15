from abc import ABC, abstractmethod
from time import time

class Plannifier(ABC):

    def __init__(self, domain):
        self.domain = domain
        self.actions = domain.action_dic

    def solve(self):
        pass
    
    
def distance_one(from_, to_):
    return 1
    
class AlphaStarPlannifier(Plannifier):
    # TODO : we could handle the ancestors through an attribute of the class ancestors = Dict(State,List(State))
    
    def __init__(self, domain, heuristic_fn, dist_fn=distance_one):
        self.domain = domain
        self.actions = domain.action_dic
        self.heuristic_fn = heuristic_fn # S -> R : heuristic distance to end
        self.dist_fn = dist_fn # S x S -> R : distance between the states
        # list of (node, distance_to_start, value, ancestors) ordered by ascending value
        # (value = distance_to_start + heuristic_to_end)
        self.nodes = []
        self.explored = []
        
    def solve(self):
        t = time()
        init = self.domain.current_state 
        # initialize tree search with init state, distance to start 0, heuristic to end, 
        # empty list of moves to get there
        self.nodes = [(init, 0, self.heuristic_fn(init), [])]
        solved = init.isFinal()
        while not solved:
            new_nodes, ancestors = self.expand()
            for node, ancestors in zip(new_nodes, ancestors):
                if node.isFinal():
                    print('Plan size: {} | Number of visited nodes: {} | Solved in {}s'.format(
                        len(ancestors), len(self.explored), time()-t))
                    return ancestors
        print('NO PLAN FOUND ! Number of visited nodes: {} | Solved in {}s'.format(
                        len(self.explored), time()-t))
        return
        
    def expand(self):
        """finds the best node and adds its children to the stack of considered states
        returns: the list of added children"""
        best_node, dist, value, ancestors = self.nodes.pop() # get our best current node
        if best_node.state in self.explored:
            return [], []
        self.explored.append(best_node.state)
        children = best_node.getChildren(self.actions)
        children_ancestors = []
        children_nodes = []
        for move_type, move_args, child in children:
            move = (move_type, move_args)
            child_ancestors = ancestors + [move]
            # g(n) : distance to start = distance of parent to start + distance of child to parent
            child_dist = dist + self.dist_fn(best_node, child)
            # h(n) : (estimated) distance to end
            child_heur = self.heuristic_fn(child)
            child_value = child_dist + child_heur
            self.insert_node(child, child_dist, child_value, child_ancestors) 
            children_ancestors.append(child_ancestors)
            children_nodes.append(child)
        return children_nodes, children_ancestors
        
    def insert_node(self, node, dist, value, ancestors):
        """insert (node,value,ancestors) in the list of considered states and returns the index where it was inserted"""
        idx = 0
         # handle extreme case that will cause problems with the while
        if len(self.nodes) == 0:
            self.nodes.append((node,dist, value, ancestors))
            return 0
        if value <= self.nodes[-1][2]:
            self.nodes.append((node,dist, value, ancestors))
            return len(self.nodes)-1
        # find index where to insert the node
        while self.nodes[idx][2] > value:
            idx += 1
        self.nodes.insert(idx,(node,dist, value, ancestors))
        return idx