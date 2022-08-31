

from collections import deque

stack = deque()

print(stack)
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('a')
print(stack)
x = stack.pop()
print(stack)
print('Popped {}'.format(x))