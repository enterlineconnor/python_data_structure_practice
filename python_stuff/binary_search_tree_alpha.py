


# Alphabetical based Binary Search Tree
#       B
#      / \
#     A   C


books = [
    "In Search of Lost Time",
    "Ulysses",
    "Don Quixote",
    "Moby Dick",
    "War and Piece",
    "Hamlet",
    "Alice In Wonderland"
]

class BookBinarySearchTreeNode:
    def __init__(self, val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self,val):
        if not self.val:
            self.val = val
            return
        
        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BookBinarySearchTreeNode(val)
            return
        if self.right:
            self.right.insert(val)
            return
        self.right = BookBinarySearchTreeNode(val)
        return
    

def find_if_title_exists(root,target):
    if root is None:
        return False
    if root.val == target:
        return True
    if target < root.val:
        return find_if_title_exists(root.left,target)
    else:
        return find_if_title_exists(root.right,target)

def left_right_trav(root):
    if root is None:
        return
    left_right_trav(root.left)
    print(root.val)
    left_right_trav(root.right)

def traversal_test(root):
    if root is None:
        return
    traversal_test(root.left)
    traversal_test(root.right)
    print(root.val)

book_tree = BookBinarySearchTreeNode()
for i in books:
    book_tree.insert(i)


# print(find_if_title_exists(book_tree,"Hamlet"))

left_right_trav(book_tree)
print('===')
traversal_test(book_tree)



    
