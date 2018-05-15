#!/home/francisco/.pyvenv/mypython3/bin/python3
# -*- coding: utf-8 -*-

"""
This module implement a DFS class who apply Depth First Search for graph:
"""

from sys import maxsize
from collections import deque
from graphs.graph_implement import create_graph, terminal_edges_list
from graphs.dfs import create_graph, topological_sort

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adj = []
        self.father = None
        self.distance = 0
        self.alarm = maxsize


def kruskal(graph):
    pass


if __name__ == '__main__':
    graph = {'r': ['s', 't'], 's': ['t', 'x'], 't': ['x', 'y', 'z'], 'x': ['y', 'z'], 'y': ['z'], 'z': []}
    edges = {('r', 's'): 5, ('r', 't'): 3, ('s', 't'): 2, ('s', 'x'): 6, ('t', 'x'): 7, ('t', 'y'): 4, ('t', 'z'): 2, ('x', 'y'): -1, ('x', 'z'): 1, ('y', 'z'): -2}
    # dag_shortest_paths(graph, edges)


def dag_shortest_paths(graph, edges={}, directed_graphs=True):
    if not edges:
        edges = terminal_edges_list(graph, directed_graphs)
    print(edges)

    ts = topological_sort(graph)

    vertices = deque()
    for x in ts:
        vertices.append(x.name)
    ts = None

    graph, _ = create_graph(graph, Vertex)
    start = graph[vertices[0]]
    start.distance = 0

    for x in vertices:
        v = graph[x]
        adj = v.adj
        for y in adj:
            u = graph[y]
            w = edges[(v.name, y)]
            if w < u.alarm:
                u.distance = w
                u.alarm = w
                u.father = v.name

    for x in graph:
        v = graph[x]
        print(v.father, v.name, v.distance)