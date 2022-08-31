


class TrieNode:
    """ A node for trie structure """

    def __init__(self,char):
        # Value. The character stored in the node
        self.char = char

        # Whether this can be the end of a word
        self.is_end = False

        # A counter indicating how many times a word is inserted
        # (if this node's is_end is true)
        self.counter = 0

        # a dictionary of child nodes
        # keys are the characters, values are the nodes
        self.children = {}



class Trie(object):
    """ The trie object """

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")
    
    def insert(self,word):
        """ Insert a word into the trie """

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1
    
    def dfs(self,node,prefix):
        """ 
        Depth-first traversal of the trie 

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a word while traversing the trie

        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """
        Given an input (a prefix), retrieve all words stored in
        the trie with the prefix, sort the words by the number of times they have been inserted
        """

        # Use a variable within the class to keep all possible outputs
        # A there can be more than one word with such prefix
        
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # Cannot find the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)


t = Trie()
t.insert("was")
t.insert("word")
t.insert("war")
t.insert("what")
t.insert("what")
t.insert("what")
t.insert("what")
t.insert("where")
print(t.query("wh"))
t.insert("where")
t.insert("where")
t.insert("where")
t.insert("where")
t.insert("where")
t.insert("where")
t.insert("where")
t.insert("where")
print(t.query("wh"))
