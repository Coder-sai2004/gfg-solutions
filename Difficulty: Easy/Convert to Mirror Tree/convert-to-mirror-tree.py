''' Structure of Binary Tree Node
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def mirror(self, root):
        
        def invert(root):
            if root is None:
                return
            
            root.left,root.right = root.right,root.left
            
            invert(root.left)
            invert(root.right)
            
        invert(root)