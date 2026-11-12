'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''

class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        res = []
        def check(root,k):
            if root is None:
                return
            
            res.append((abs(k - root.data)))
            
            check(root.left,k)
            check(root.right,k)
            
        check(root,k)
        
        return min(res)