'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def merge(self, r1: 'Node', r2: 'Node') -> list[int]:
        res = []
        
        def check(root):
            if root is None:
                return 
            
            res.append(root.data)
            
            check(root.left)
            check(root.right)
            
        check(r1)
        check(r2)
        
        return sorted(res)