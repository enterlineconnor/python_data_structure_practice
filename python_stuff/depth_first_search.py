
"""
Depth-First Search "hello world"

depth-first search is considered a "stack" data structure 

['a', 'b', 'd', 'f', 'c', 'e']

['a', 'c', 'e', 'b', 'd', 'f']

These are both perfectly good examples of a depth first search on the "graph"
dictionary used in these functions.

The main key of the depth first search is that it explores the entire path of the sources children before
moving to the next child in the stack

for example:

graph = {
    'a': ['c','b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

with 'a' as source branch:

    dps = ['a', 'b', 'd', 'f', 'c', 'e'] or ['a', 'c', 'e', 'b', 'd', 'f']

'a' is our source node here, which means its children are 'b' and 'c'

notice that, in both situations, 'b' and 'c' are not next to each other.

The key here is that they are ALWAYS next to 'a'

the reason for this is the entire path of b or c is drilled through before the other of the two children's
paths are searched. 

This happens throughout the entirety of the search, and is not unique to the 'a' node

"""


def dfs(graph,source) -> list[int]:
    stack, dfs_order = [source], []
    while len(stack) > 0:
        current = stack.pop()
        dfs_order.append(current)
        for neighbor in graph[current]:
            stack.append(neighbor)
    return(dfs_order)

"""
Recursive Depth-First Search

graph = the graph relationship between nodes
source = parent node being used to evaluate neighbors
dfs_order = array used to aggregate resulting neighbors for list return

the recursive function takes a starting point, then searches for all that starting points neighbors,
and recalls the recursive function for each neighbor

this leads to the stack completing one "path" of the tree in it's entirety before moving to the second child branch

"""
def recursive_dfs(graph,source,dfs_order = []) -> list[int]:
    dfs_order.append(source)
    for neighbor in graph[source]:
        recursive_dfs(graph,neighbor)
    return dfs_order


graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

dfs, rec = dfs(graph,'a'),recursive_dfs(graph,'a')
print(dfs)
print('=================')
print(rec)
print('=================')

