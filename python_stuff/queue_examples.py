


# Reverse string with Queue and Stack structure



from inspect import stack
import queue


my_string = 'abcdef'

list_string = list(my_string)
queue_order = ''
while list_string:
    queue_order += list_string.pop(0)

print(queue_order)

queue_list = list(queue_order)

stack_order = ''
while queue_list:
    stack_order += queue_list.pop()
print(stack_order)


    