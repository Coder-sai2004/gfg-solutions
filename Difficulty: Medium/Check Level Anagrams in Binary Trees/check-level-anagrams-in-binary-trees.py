"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""

from collections import Counter
class Solution:

    def areAnagrams(self, root1, root2):
        l = []
        r = []
        
        def order(root,level,res):
            if root is None:
                return 
            
            if len(res) <= level:
                res.append([])
                
            res[level].append(root.data)
            
            order(root.left,level + 1,res)
            order(root.right,level + 1,res)
            
        order(root1,0,l)
        order(root2,0,r)
        
        return len(l) == len(r) and all(Counter(x) == Counter(y) for x,y in zip(l,r))