from typing import Sized
import numpy as np
import math


def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
    stack = []
    path=[]
    visited={}
    visited[start] = 1 
    stack.append(start)
    while stack: 
        i = stack.pop()
        path.append(i)

        if i == end:
            print(visited.items())
            print(path)
            return visited, path

        
        for j in range (len(matrix[i])):
            if matrix[i][j] != 0 and j not in path:
                stack.append(j)
                visited[j] = i
            


def BFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path=[]
    visited={}
    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        i = queue[0]
        path.append(i)
        queue.remove(queue[0])

        if i == end:
            print(visited.items())
            print(path)
            return visited, path

        for j in range (len(matrix[i])):
            if matrix[i][j] != 0 and j not in visited:
                queue.append(j)
                visited[j] = i

def min_index(cost, path):
    min = 100
    index = 0
    for i in range(len(cost)):
        if cost[i] < min and i not in path:
            min = cost[i]
            index = i
    return index


def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    size = len(matrix[start])
    path = []
    visited = {}
    cost = []
    for i in range(size):
        cost.append(100)
    cost[start] = 0
    queue = []
    queue.append(start)
    visited[start] = start

    while queue: 
        v = min_index(cost, path)
        print('chosing ', v)
        queue.remove(v)
        path.append(v)

        if v == end:
            print(visited)
            path = []
            t = end
            while t != start:
                path.append(t)
                t = visited[t]
            path.append(start)
            print(path)

            return visited, path
        
        for j in range(size):
            if matrix[v][j] != 0 and j not in path:
                queue.append(j)
                if cost[j] > cost[v] + matrix[v][j]:
                    visited[j] = v
                    cost[j] = cost[v] + matrix[v][j]
                    print('cost ', j , '= ', cost[j])


def h(matrix, end):
    n = len(matrix[0])
    source = matrix [:]
    queue = []
    queue.append(end)
    
    i = 1
    while queue:
        v = queue[0]
        queue.remove(v)
        for j in range(n):
            if matrix[v][j] != 0:
                source[v][j] = i
            else: 
                source[i][j] = 0
        i += 1
    return source



def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    n = len(matrix[0])
    source = [n]*n
    source = h(matrix, end)
    size = len(matrix[start])
    path = []
    visited = {}
    cost = []
    for i in range(size):
        cost.append(100)
    cost[start] = 0
    queue = []
    queue.append(start)
    visited[start] = start

    while queue: 
        v = min_index(cost, path)
        print('chosing ', v)
        queue.remove(v)
        path.append(v)

        if v == end:
            print(visited)
            path = []
            t = end
            while t != start:
                path.append(t)
                t = visited[t]
            path.append(start)
            print(path)
            return visited, path
        
        for j in range(size):
            if source[v][j] != 0 and j not in path:
                queue.append(j)
                if cost[j] > cost[v] + source[v][j]:
                    visited[j] = v
                    cost[j] = cost[v] + source[v][j]
                    print('cost ', j , '= ', cost[j])

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path = []
    visited = {}
    size = len(matrix[start])
    
    cost = []
    for i in range(size):
        cost.append(100)

    cost[start] = 0
    source = [size]*size
    source = h(matrix, end)
    queue = []
    queue.append(start)
    visited[start] = start

    while queue: 
        v = min_index(cost, path)
        print('chosing ', v)
        queue.remove(v)
        path.append(v)

        if v == end:
            print(visited)
            path = []
            t = end
            while t != start:
                path.append(t)
                t = visited[t]
            path.append(start)
            print(path)

            return visited, path
        
        for j in range(size):
            if matrix[v][j] != 0 and j not in path:
                queue.append(j)
                if cost[j] > cost[v] + matrix[v][j] + source[v][j]:
                    visited[j] = v
                    cost[j] = cost[v] + matrix[v][j] +  source[v][j]
                    print('cost ', j , '= ', cost[j])
    
    
    
