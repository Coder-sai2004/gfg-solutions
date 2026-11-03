''' Binary Tree Node Structure
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None'''


class Solution:

    def maxLevel(self, root: "Node") -> int:
        
        def check(root,level):
            if root is None:
                return level
            
            l = check(root.left,level + 1)
            r = check(root.right,level + 1)
            
            return max(l,r)
            
        return check(root,0)