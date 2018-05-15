#!/home/francisco/.pyvenv/mypython3/bin/python3
# -*- coding: utf-8 -*-

"""
This module implement a DFS(Depth First Search) function for a graph.
It also implements a topological ordering function and another to find a strongly connected connection.
"""
from graphs.graph_implement import *


class DFSVertex():
    """
    Implement a vertex structure for DFS.

    Attributes:
        name: the name of vertex.
        adj: a list of adjacent __vertices for this vertex.
        visit: if ___graph is visited by dfs method.
        ini_time: the __time that vertex is discover.
        end_time: the time that vertex go out of queue.
        parent: the parent of vertex in dfs tree.
        ccnum: the connected component, a number that shows which vertex path is connected.

    Parameter:
        name (str): the name o vertex.
    """
    def __init__(self, name):
        self.name = name
        self.adj = []
        self.visit = 0
        self.ini_time = 0
        self.end_time = 0
        self.parent = None
        self.ccnum = 0


time = 0
cc = 0


def explore(graph, u):
    """
    Assist the dfs method to scroll through adjacent vertices.

    Args:
        u (DFSVertex): the vertex where dfs start.
    """
    global time
    time += 1
    u.ini_time = time
    u.ccnum = cc

    u.visit = 1

    for i in u.adj:
        if i:
            v = graph[i]
            if v.visit == 0:
                v.parent = u.name
                v.visit = 1
                explore(graph, v)

    time += 1
    u.end_time = time


def dfs(graph):
    """
    Create a DFS structure.

    Parameter:
        graph (dict): a dictionary where the keys are names of vertices and values are their lists of adjacent.

    Return:
        A DFS structure.
    """
    global cc

    graph, vertices = create_graph(graph, DFSVertex)

    v = input('Enter the start vertex or none for start with first vertex: ')
    if not v:
        v = vertices[0]

    try:
        v = graph[v]
    except KeyError:
        print('This vertex does not exist.')

    cc += 1
    explore(graph, v)

    for i in vertices:
        u = graph[i]
        if u.visit == 0:
            cc += 1
            explore(graph, u)

    dfs_structure = []
    for x in graph:
        dfs_structure.append(graph[x])

        dfs_structure.sort(key=lambda c: c.ccnum)

    return dfs_structure


def topological_sort(graph):
    """
    Create a topological order.

    Parameter:
        graph (dict): a dictionary where the keys are names of vertices and values are their lists of adjacent.

    Return:
        A list of DFSVertex objects in topological order.
    """
    topological_structure = dfs(graph)
    topological_structure.sort(key=lambda c: c.end_time, reverse=True)

    return topological_structure


def strongly_cc(graph):
    """
    Find the strongly connected components in graph.

    Parameter:
        graph (dict): a dictionary where the keys are names of vertices and values are their lists of adjacent.

    Return:
        A strongly connected components structure.
    """
    dfs_structure = topological_sort(graph)
    vertices = deque()
    for v in dfs_structure:
        vertices.append(v.name)

    re_graph, _ = revert_graph(graph)
    graph, _ = create_graph(re_graph, DFSVertex)

    global time
    global cc
    time = 0
    cc = 0
    for i in vertices:
        u = graph[i]
        if u.visit == 0:
            cc += 1
            explore(graph, u)

    strongly_cc_structure = []
    for x in graph:
        strongly_cc_structure.append(graph[x])

        strongly_cc_structure.sort(key=lambda c: c.ccnum)

    return strongly_cc_structure


if __name__ == '__main__':
    # graph = {'A': ['B', 'C'], 'B': ['E'], 'C': ['D'], 'D': ['A', 'H'], 'E': ['F', 'G', 'H'], 'F': ['B', 'G'], 'G': [],
    #           'H': ['G']}
    #
    # graph = {'cuecas':['calças', 'sapatos'], 'calças':['cinto', 'sapatos'], 'cinto':['paleto'], 'camisa':['gravata',
    #           'cinto'], 'gravata':['paleto'], 'paleto':[], 'meias':['sapatos'], 'sapatos':[]}

    graph = {'A':['B'], 'B':['C', 'D', 'E'], 'C':['F'], 'D':[], 'E':['B', 'F', 'G'], 'F':['C', 'H'], 'G':['H', 'J'],
              'H':['K'], 'I':['G'], 'J':['I'], 'K':['L'], 'L':['J']}

    # graph = {'A':[], 'B':['A', 'E'], 'C':['B', 'F'], 'D':['B'], 'E':['B'], 'F':['C', 'E'], 'G':['E', 'I'],
    #           'H':['G', 'F'], 'I':['J'], 'J':['G', 'L'], 'K':['H'], 'L':['K']}

    # graph = {'A':['B', 'E'], 'B':['A'], 'C':['D', 'G', 'H'], 'D':['C', 'H'], 'E':['A', 'I', 'J'], 'F':[],
    #          'G':['C', 'H', 'K'],'H':['C', 'D', 'G', 'K', 'L'], 'I':['E', 'J'], 'J':['E', 'I'], 'K':['G', 'H'],
    #          'L':['H']}

    # dfs = dfs(graph)
    # print('DFS structure:')
    # for t in dfs:
    #     print(t.name)
    #     print('ccnum: {0}, parent: {1}\ninit: {2}, end: {3}\n'.format(t.ccnum, t.parent, t.ini_time, t.end_time))

#
    # dfs = topological_sort(graph)
    # print('Topological order:')
    # for t in dfs:
    #     print(t.name, end=' ')
    # print()

    graph = {'a':['b'], 'b':['c', 'f', 'e'], 'c':['d', 'g'], 'd':['c', 'h'], 'e':['a', 'f'], 'f':['g'], 'g':['f', 'h'],
             'h':['h']}
    sdfs = strongly_cc(graph)
    for t in sdfs:
        print(t.name)
        print('ccnum: {0}, parent: {1}\ninit: {2}, end: {3}\n'.format(t.ccnum, t.parent, t.ini_time, t.end_time))
