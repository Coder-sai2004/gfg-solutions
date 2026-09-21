'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def rightView(self, root):
        res = []
        
        def invert(root):
            if root is None:
                return
            
            root.left,root.right = root.right,root.left
            invert(root.left)
            invert(root.right)

        def order(root,level,res):
            if root is None:
                return

            if len(res) == level:
                res.append(root.data)

            order(root.left,level + 1,res)
            order(root.right,level + 1,res)
            
            
        invert(root)
        order(root,0,res)

        return res