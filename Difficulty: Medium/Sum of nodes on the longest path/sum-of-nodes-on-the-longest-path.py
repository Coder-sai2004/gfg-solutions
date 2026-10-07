'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''
from collections import defaultdict
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        res = defaultdict(list)
        def check(root,s,level):
            if root is None:
                return 0
            
            s += root.data
            
            if root.left is None and root.right is None:
                res[level].append(s)
                
            left = check(root.left,s,level + 1)
            right = check(root.right,s, level + 1)
            
        check(root,0,0)
        
        key = max(res.keys())
        return max(res[key])