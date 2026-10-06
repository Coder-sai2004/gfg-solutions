"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        
        def deep(root):
            
            if root.left is None:
                return root.data
                
            return deep(root.left)
            
        return deep(root)