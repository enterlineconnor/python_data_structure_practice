

from audioop import reverse


class Node:
    # constructor
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,val):
        new_node = Node(val)
        if self.head:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def print_ll(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next
    
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.print_ll()
LL.reverse()
print('--------------')
LL.print_ll()
