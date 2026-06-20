"""Some terminology 

agent: an entity that perceives and acts in an environment.
state: a configuration of the agent and its environment.
initial state: the state in which the agent starts.
action: a change in th state of the agent or its environment.
    we use a function ACTIONS(s) to return the set of actions that can be executed in state s.
RESULT(s,a) is a transition model
    s is current state, a is an action, and RESULT(s,a) is the state that results from doing a in s.
goal test: a function that returns true when the state is goal state.
path cost: a function that assigns a numeric cost to each path. The problem is to find a least-cost solution.
optimal solution: a solution with the lowest path cost.
to implement a search algorithm, we use a data structure called and name it node. 
    a node contains 
    1. state    2. parent node 3. action 4. path cost       

    main algorithm for search is as follows:    
        start with a frontier that contains the initial state
        loop
            if frontier is empty,then no solution
            remove a node from the frontier 
            if node contains a goal state then return the corresponding solution
            expand the node, adding the resulting nodes to the frontier

            
types of frontier:
    stack: last in first out
    depth first search: 
    breadth first search:
    queue: first in first out


types of search algos:
    uninformed search: 
        breadth first search
        uniform cost search
        depth first search
        depth limited search
        iterative deepening search

    informed search:
        greedy best first search   -- it estimates the cost to reach the goal from node n, and expands the node that is estimated to be closest to the goal.
            by giving every node a heuristic value h(n) that estimates the cost of the cheapest path from n to a goal, greedy best first search expands the node with the lowest h(n) value.
        a* search   ---  a* also uses a heuristic function, but it combines the cost to reach the node and the estimated cost to reach the goal.
            matlab kitta dur jana h Plus kitta dur aa chuke h
"""