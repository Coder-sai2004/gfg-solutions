''' Structure of Binary Tree Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        
        def depth(root,level):
            if root is None:
                return level
            
            
            l = depth(root.left,level + 1)
            r = depth(root.right,level + 1)
            
            return max(l,r)
        
        return depth(root,0) - 1