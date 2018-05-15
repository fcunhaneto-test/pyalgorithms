#!/home/francisco/.pyvenv/mypython3/bin/python3
# -*- coding: utf-8 -*-

"""
This module implement a BFS (Breadth First Search) function for a graph.
"""
from collections import deque
from graphs.graph_implement import create_graph


class BFSVertex():
    """
    Implement a vertex structure for BFS.

    Attributes:
        name: the name of vertex.
        adj: a list of adjacent __vertices for this vertex.
        visit: if graph is visited by dfs method.
        father: the parent of vertex in dfs tree.
        distance: the distance between the given vertex and the current vertex.

    Parameter:
        name (str): the name o vertex.
    """

    def __init__(self, name):
        self.name = name
        self.adj = []
        self.visit = 0
        self.father = None
        self.distance = 0


def bfs(gdict):
    """
    Create a BFS structure.

    Parameter:
        gdict (dict): a dictionary where the keys are names of vertices and values are their lists of adjacent.

    Return:
        A BFS structure.
    """
    q = deque()
    graph, vertices = create_graph(gdict, BFSVertex)

    v = input('Enter the start vertex or none for start with first vertex: ')
    print()
    if not v:
        v = vertices[0]

    try:
        v = graph[v]
    except KeyError:
        print('This vertex does not exist.')

    print(v)
    v.visit = 1
    q.append(v)
    while q:
        u = q.popleft()

        for a in u.adj:
            s = graph[a]
            if s.visit == 0:
                s.visit = 1
                s.distance = u.distance + 1
                s.father = u.name
                q.append(s)

    return graph

if __name__ == '__main__':
    graph = {'E':['S', 'D'], 'D':['E', 'S'], 'S':['E', 'D', 'A', 'C'], 'C':['S', 'B'], 'A':['S', 'B'], 'B':['A', 'C']}
    # graph = {'r':['s', 'v'], 's':['r', 'w'], 't':['u', 'w', 'x'], 'u':['t', 'x', 'y'], 'v':['r'], 'w':['s', 't', 'x'],
    #          'x':['t', 'u', 'w', 'y'], 'y':['u', 'x']}
    b = bfs(graph)

    for a in b:
        v = b[a]
        print(v.name)
        print('parent: {0}, distance: {1}'.format(v.father, v.distance))
