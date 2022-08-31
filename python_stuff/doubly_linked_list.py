

class Node:
    # constructor
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
    
    # def insert(self,val):
    #     new_node = Node(val)
    #     if self.head:
    #         current = self.head
    #         while(current.next):
    #             current = current.next
    #         current.next = new_node
    #     else:
    #         self.head = new_node
    
    # def print_ll(self):
    #     current = self.head
    #     while(current):
    #         print(current.val)
    #         current = current.next


