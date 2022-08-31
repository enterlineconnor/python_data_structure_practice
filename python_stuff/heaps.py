


import heapq

needs_a_good_heapen = [-21,-1,-45,-78,-3,-5]

def left_child(index):
    return (index * 2) + 1

def right_child(index):
    return (index * 2) + 2

def find_parent(index):
    return int((index - 1) / 2)

heapq.heapify(needs_a_good_heapen)

print(needs_a_good_heapen)

heapq.heappop(needs_a_good_heapen)

print(needs_a_good_heapen)

heapq.heappush(needs_a_good_heapen,-25)

print(needs_a_good_heapen)

# 21 is at index 1, so it's children should be (1*2)+1 and (1*2)+2
print('index 1 left child: {}'.format(needs_a_good_heapen[left_child(1)]))
print('index 1 right child: {}'.format(needs_a_good_heapen[right_child(1)]))


# 5 is at index 5, so it's parent should be at (5-1)/2
print('index 5 parent: {}'.format(needs_a_good_heapen[find_parent(5)]))
