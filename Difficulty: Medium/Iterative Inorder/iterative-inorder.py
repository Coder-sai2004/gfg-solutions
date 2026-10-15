# Definition for Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def inOrder(self, root):
        res = []
        def check(root):
            if root is None:
                return 
            
            check(root.left)
            res.append(root.data)
            check(root.right)
            
        check(root)
        
        return res