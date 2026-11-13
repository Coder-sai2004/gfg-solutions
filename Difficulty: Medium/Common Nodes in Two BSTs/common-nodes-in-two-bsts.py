''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        res = []
        s = set()
        
        def check(root):
            if root is None:
                return 
            
            s.add(root.data)
            
            check(root.left)
            check(root.right)
        
        def find(root,s):
            if root is None:
                return
            
            if root.data in s:
                res.append(root.data)
                
            find(root.left,s)
            find(root.right,s)
        
        check(r1)
        find(r2,s)
        
        if res:
            return sorted(res)
        return []