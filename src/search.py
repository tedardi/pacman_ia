'''
Nome: Marcello Vannucci Tedardi
NºUSP: 5924945
Data: 23/04/2018
'''


# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
   
    # cabecalho para facilitar a compreenssao da implementacao
    start = problem.getStartState()
    start = (start, "South", 1)
    sucessores = problem.getSuccessors(problem.getStartState())
    print "Inicio:", start[0]
    print "Sucessores:"
    print "........ posicao  acao  peso"
    for s in sucessores:
        print "........", s
        print "...... cost of action", problem.getCostOfActions({s[1]})


    ##############################################################################

    # busca em profundidade
    print "\n\nCOMENCANDO O CODIGO: ...\n"
    print "Iniciando a busca em profundidade ...\n"

    from game import Directions

    South = Directions.SOUTH
    West = Directions.WEST
    North = Directions.NORTH
    East = Directions.EAST
   
    # Variaveis
    visitados = []
    solucao = []
    resultado = []
    borda = util.Stack()
    custo = []

    # Inicio o algoritmo com o estado inicial
    start = problem.getStartState()
    start = (start, resultado, 0)
    borda.push(start)
   
    while borda:
        no = borda.pop()

       
        if problem.isGoalState(no[0]):
           
            return no[1]
        if no[0] not in visitados:
            visitados.append(no[0])
           
            sucessores = problem.getSuccessors(no[0]) 
            for s in sucessores:
                resultado = no[1] + [s[1]]
                solucao.append(resultado)
                custo = no[2] + s[2]
                borda.push((s[0],resultado,custo))


def breadthFirstSearch(problem):
   
    print "\n\nCOMENCANDO O CODIGO: ...\n"
    print "Iniciando a busca em largura ...\n"


    from game import Directions

    South = Directions.SOUTH
    West = Directions.WEST
    North = Directions.NORTH
    East = Directions.EAST
   

    # Variaveis
    visitados = []
    solucao = []
    resultado = []
    borda = util.Queue()
    custo = []

    # Inicio o algoritmo com o estado inicial
    start = problem.getStartState()
    start = (start, resultado, 0)
    borda.push(start)
   
    while borda:
        no = borda.pop()
      
        if problem.isGoalState(no[0]):
            print "No...", no[1]
            
            return no[1]
        if no[0] not in visitados:
            visitados.append(no[0])
           
            sucessores = problem.getSuccessors(no[0]) 
            for s in sucessores:
                resultado = no[1] + [s[1]]
                solucao.append(resultado)
                custo = no[2] + s[2]
                borda.push((s[0],resultado,custo))


def uniformCostSearch(problem):
    print "\n\nCOMENCANDO O CODIGO: ...\n"
    print "Iniciando a busca em custo uniforme ...\n"

    from game import Directions

    South = Directions.SOUTH
    West = Directions.WEST
    North = Directions.NORTH
    East = Directions.EAST
   
    # Variaveis
    visitados = []
    #solucao = []
    resultado = []
    borda = util.PriorityQueue()
    custo = []

    # Inicio o algoritmo com o estado inicial
    start = problem.getStartState()
    start = (start, resultado, 0)
    borda.push(start, 0)
   
    while borda:
        no = borda.pop()
        
        if problem.isGoalState(no[0]):
            print "No...", no[1]
       
            return no[1]
  
        if no[0] not in visitados:
            visitados.append(no[0])
           
            sucessores = problem.getSuccessors(no[0]) 
            for s in sucessores:
                custo = no[2] + s[2] # adiciono de forma iterativa o custo
                resultado = no[1] + [s[1]]  # adiciono de forma iterativa o caminho
                
                borda.push((s[0],resultado,custo), custo)
    
    
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    
    print "\n\nCOMENCANDO O CODIGO: ...\n"
    print "Iniciando a busca A estrela ...\n"

    from game import Directions

    South = Directions.SOUTH
    West = Directions.WEST
    North = Directions.NORTH
    East = Directions.EAST
   
    # Variaveis
    visitados = []
    resultado = []
    borda = util.PriorityQueue()
    custo = []

    # Inicio o algoritmo com o estado inicial
    start = problem.getStartState()
    start = (start, resultado, 0)
    heuristica =  heuristic(problem.getStartState(), problem)
    borda.push(start, 0 + heuristica)
   
    while borda:
        no = borda.pop()
        
        if problem.isGoalState(no[0]):
            return no[1]
  
        if no[0] not in visitados:
            visitados.append(no[0])
            sucessores = problem.getSuccessors(no[0]) 
            for s in sucessores:
                custo = no[2] + s[2] # adiciono de forma iterativa o custo
                resultado = no[1] + [s[1]]  # adiciono de forma iterativa o caminho
                borda.push((s[0],resultado,custo), custo + heuristic(no[0], problem))
    
def learningRealTimeAStar(problem, heuristic=nullHeuristic):
    """Execute a number of trials of LRTA* and return the best plan found."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    # MAXTRIALS = ...
    

# Abbreviations 
# *** DO NOT CHANGE THESE ***
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
lrta = learningRealTimeAStar
