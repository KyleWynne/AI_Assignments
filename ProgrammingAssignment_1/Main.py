from search import *

def Alphabet_Search():
    #create a graph for the problem from the homework with each node and the weights
    Alphabet_Map = UndirectedGraph(dict(
        S=dict(A=3, B=1, C=8),
        A=dict(D=3, E=7, G=15),
        B=dict(G=20),
        C=dict(G=5),
        D=dict(),
        E=dict(),
        G=dict()))
    
    #define the problem with the problem function
    Alphabet_problem = GraphProblem('S', 'G', Alphabet_Map)

    #execute the breadth first search
    a = breadth_first_graph_search(Alphabet_problem)

    #create a stack and add the output node of the search
    nodes = []
    nodes.append(a)
    i = 0

    #extract the path the node took by using the parent function and 
    #a loop to catch the type error when we find the root
    while 1:

        try:
            temp = nodes.pop()
            nodes.append(temp)
            tester = temp.parent
            tester.state
            i+=1
            nodes.append(tester)

        except AttributeError:
            break

    j=0

    print("solution Path: ")
    #pop and print the solution path in the correct order
    while 1:
        if j > i:
            break

        temp = nodes.pop()
        print(temp.state)
        j+=1

    pass

#search the romania map from class
def Romania_Search():
    #create a graph with the weights from the map
    romania_map = UndirectedGraph(dict(
        Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
        Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
        Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
        Drobeta=dict(Mehadia=75),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99),
        Hirsova=dict(Urziceni=98),
        Iasi=dict(Vaslui=92, Neamt=87),
        Lugoj=dict(Timisoara=111, Mehadia=70),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97),
        Rimnicu=dict(Sibiu=80),
        Urziceni=dict(Vaslui=142)))
    #define the problem
    romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
    #execute the search
    a = breadth_first_graph_search(romania_problem)
    #create a stack and input the output from the search
    nodes = []
    nodes.append(a)
    i = 0
    #iteratively use the parent function to work back through the solution path to the root
    while 1:

        try:
            temp = nodes.pop()
            nodes.append(temp)
            tester = temp.parent
            tester.state
            i+=1
            nodes.append(tester)
        #breaks when a node doesnt have a parent
        except AttributeError:
            break

    j=0

    print("solution Path: ")
    #print the solution path in the correct order with the stack
    while 1:
        if j > i:
            break

        temp = nodes.pop()
        print(temp.state)
        j+=1



#run both searches and add enters for readability
print("\nBreadth First Search \n")
print("First Search From S->G")
Alphabet_Search()
print("\nSearch From Arad to Bucharest")
Romania_Search()
print("\n")