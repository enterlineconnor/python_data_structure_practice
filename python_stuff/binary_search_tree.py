


from sympy import true


class BinarySearchTreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.left = left
        self.right = right
        self.val = val


    def insert(self, val):

        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BinarySearchTreeNode(val)
            return
        
        if self.right:
            self.right.insert(val)
            return

        self.right = BinarySearchTreeNode(val)
        return


node_1 = BinarySearchTreeNode(25)
node_2 = BinarySearchTreeNode(75)
node_3 = BinarySearchTreeNode(40,node_1,node_2)

node_4 = BinarySearchTreeNode(90)
node_5 = BinarySearchTreeNode(110)
node_6 = BinarySearchTreeNode(100,node_4,node_5)


root = BinarySearchTreeNode(80,node_3,node_6)


def binary_tree_search(root,target):
    if root is None or root.val == target:
        return root
    print(root.val)
    if target < root.val:
        return binary_tree_search(root.left,target)
    
    else:
        return binary_tree_search(root.right,target)
    




if binary_tree_search(root,300):
    print(True)
else:
    print(None)

root.insert(300)

if binary_tree_search(root,300):
    print(True)
else:
    print(None)