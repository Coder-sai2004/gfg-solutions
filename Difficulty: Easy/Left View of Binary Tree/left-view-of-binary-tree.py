''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

class Solution:
    def leftView(self, root):
        res = []
        
        def order(root,level,res):
            if root is None:
                return
            
            if len(res) == level:
                res.append(root.data)
                
            order(root.left,level + 1,res)
            order(root.right,level + 1,res)
            
        order(root,0,res)
        
        return res