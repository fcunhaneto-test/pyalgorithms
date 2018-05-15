from collections import deque


def create_graph(gdict, obj):
    """
    Create a graph from the given dictionary.

    Args:
        gdict (dict): a dictionary where keys is vertex name and values are adjacent list for this vertex.
    """
    vertices = deque(gdict)
    graph = {}
    for name in vertices:
        vertex = obj(name)
        vertex.adj = gdict[name]
        graph[name] = vertex

    return graph, vertices


def revert_graph(gdict):
    graph = {}
    vertices = deque(gdict)
    for v in vertices:
        graph[v] = []

    for v in vertices:
        adj = gdict[v]
        for a in adj:
            graph[a].append(v)

    return graph, vertices


def terminal_adjacent_list():
    """
    Entry by terminal the vertices and its adjacency lists.

    Return:
         A dictionary where keys are vertices and values are they adjacent list.
    """
    num = 0
    vertices = deque()
    graph = {}

    print('Input the vertices name, none for stop:')
    while True:
        num += 1
        name = input('enter name for vertex {0}: '.format(num))
        if not name:
            break

        vertices.append(name)

    print('\nInput the vertex adjacent name, none for stop:')
    for v in vertices:
        adj = []
        num = 0

        print('\n*********************************************')
        print('Input the vertex adjacent for {0}:'.format(v))
        while True:
            num += 1
            name = input('adjacent {0}: '.format(num))
            if not name:
                if num == 1:
                    adj = []
                break

            adj.append(name)

        graph[v] = adj

    return graph


def terminal_edges_list(graph={}, directed_graphs=True):
    """
    Entry by terminal the vertices and its edges.

    Return:
         A list that contain a tuple with vertex of edge and weight.
    """
    edges = {}

    if not graph:
        print('Input the edges, none for stop:')
        while True:
            print('*****************************')
            v1 = input('the start vertex: ')
            if not v1:
                break
            v2 = input('the end vertex: ')
            w = int(input('the edge weight: '))
            print('*****************************')
            if directed_graphs:
                edges[(v1, v2)] = w
            else:
                edges[(v1, v2)] = w
                edges[(v2, v1)] = w
    else:
        for x in graph:
            adj = graph[x]
            print('*****************************')
            for a in adj:
                w = int(input('{0} --> {1} weight: '.format(x, a)))
                if directed_graphs:
                    edges[(x, a)] = w
                else:
                    edges[(x, a)] = w
                    edges[(a, x)] = w


    return edges


if __name__== '__main__':
    graph = {'A': ['B', 'C'], 'B': ['E'], 'C': ['D'], 'D': ['A', 'H'], 'E': ['F', 'G', 'H'], 'F': ['B', 'G'], 'G': [],
              'H': ['G']}

    e = terminal_edges_list(graph)
    print(e)