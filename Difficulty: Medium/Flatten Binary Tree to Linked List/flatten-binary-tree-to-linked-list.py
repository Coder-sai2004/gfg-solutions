""" Binary Tree Node Structure
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""
class Solution:
    def flatten(self, root):
        st = []
        def check(root):
            if root is None:
                return 
            
            if root.left and root.right:
                st.append(root.right)
                root.right = root.left
                root.left = None
            elif root.left:
                root.right = root.left
                root.left = None
                
            
            if root.right is None and st:
                root.right = st.pop()
            
            check(root.right)
            
        check(root)
                