'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def minDepth(self, root):
        def check(root,level):
            if root is None:
                return 100000
            
            if root and root.left is None and root.right is None:
                return level
                
            l = check(root.left,level + 1)
            r = check(root.right,level + 1)
            
            return min(l,r)
            
        return check(root,1)