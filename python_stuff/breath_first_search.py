"""
Breath-first search (bfs) is considered as 'Queue' data structure.

This is akin to a line at the super market. The priority is within the order of the data

In Depth-first search, we were able to use recursion to create our search result, but this is impossible in bfs.
Recursion implies a stack of some kind and, as we've stated, bfs is a queue, not a stack.

So, bfs is done Iterally
"""
from collections import deque

def shift(this_list):
    this_list = deque(this_list)
    this_list.rotate(-1)
    shifted_list = list(this_list)
    return shifted_list


def bfs_traversal(graph, source, bfs_out = []) -> list[int]:
    queue = [source]
    while len(queue) > 0:
        shifted = shift(queue)
        current = shifted.pop()
        queue = shifted
        bfs_out.append(current)
        for neighbor in graph[current]:
            queue.append(neighbor)
    return bfs_out



graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


bfs = bfs_traversal(graph, 'a')
print(bfs)