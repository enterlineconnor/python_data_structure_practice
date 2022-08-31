# edges = [ ['a' , 'b'] , ['a' , 'c' ], [ 'c' , 'd' ] ]

# graph = {}
# for e in edges:
# 	if graph.get(e[0]) is None:
# 		graph[e[0]] = []
# 	if graph.get(e[1]) is None:
# 		graph[e[1]] = []
# 	graph[e[0]].append(e[1])
# 	graph[e[1]].append(e[0])

# print(graph)



# edges = [ [ 'a','b'] , [ 'a' , 'c' ] , [ 'c' , 'd' ] ]


# directed_graph = {}
# for e in edges:
# 	if directed_graph.get(e[0]) is None:
# 		directed_graph[e[0]] = []
# 	directed_graph[e[0]].append(e[1])


# print(directed_graph)



# Given two nodes on the graph, determine if there is a path between two nodes 

from graphql import visit
from sympy import false, re, true


# d_graph = {

# 	'a': [ 'b' , 'c' ],
# 	'c': [ 'd' ],
# 	'e': [ 'f' ] 
# } 

# source = 'c'
# dest = 'd'

# # DFS, therefore, recursion

# def has_path(d_graph, source, dest):
# 	if source == dest:
# 		return True
# 	if d_graph.get(source):
# 		for neighbor in d_graph[source]:
# 			if has_path(d_graph,neighbor,dest):
# 				return True
# 	return False

# print(has_path(d_graph, source, dest))




# edges = [ ['a','b'] , ['a','c'] , ['c','d'] , ['e','f'] ]

# source = 'e'
# dest = 'f'


# # Given a set of edges, create a directed graph. Then, use a DFS to return True or False if there is a path between two given nodes “source” and “dest”


# def has_path(d_graph,source,dest):
# 	if source == dest:
# 		return True
# 	if d_graph.get(source):
# 		for neighbor in d_graph[source]:
# 			if has_path(d_graph,neighbor,dest):
# 				return True
# 	return False
		

# d_graph = {}
# for e in edges:
# 	if d_graph.get(e[0]) is None:
# 		d_graph[e[0]] = []
# 	d_graph[e[0]].append(e[1])


# print(has_path(d_graph,source,dest))



edges = [  [ 'a','b' ], [ 'b' , 'c'  ], [ 'c','a' ], ['c','d' ],['e','f' ]  ]

source = 'a'
dest = 'c'

def dfs_has_path(ud_graph,source,dest,visited=[]):
	print(source)
	if ud_graph.get(dest) is None or ud_graph.get(source) is None:
		print('Either Source or Destination Not in Graph')
		return False
	if source == dest:
		return True
	print('|')
	if ud_graph.get(source) and source not in visited :
		visited.append(source)
		for neighbor in ud_graph[source]:
			if dfs_has_path(ud_graph,neighbor,dest,visited):
				return True
	return False



def bfs_has_path(ud_graph, source, dest, visited=[],queue=[]):
	if ud_graph.get(dest) is None or ud_graph.get(source) is None:
		print('Either Source or Destination Not in Graph')
		return False
	if source == dest:
		return True
	visited.append(source)
	queue.append(source)
	while queue:
		current = queue.pop(0)
		print(current)
		if current == dest:
			return True
		print('|')
		for neighbour in ud_graph[current]:
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)
	return False


ud_graph = {}
for e in edges:
	if ud_graph.get(e[0]) is None:
		ud_graph[e[0]] = []
	if ud_graph.get(e[1]) is None:
		ud_graph[e[1]] = []
	ud_graph[e[0]].append(e[1])
	ud_graph[e[1]].append(e[0])


# print(ud_graph)

print(dfs_has_path(ud_graph,source,dest,visited=[]))
print(bfs_has_path(ud_graph,source,dest,visited=[]))


# def func() -> bool:
# 	x = 100

# print(func())
x = 10
y = 10

def test(x,y):
	return x is y

print(test(x,y))

