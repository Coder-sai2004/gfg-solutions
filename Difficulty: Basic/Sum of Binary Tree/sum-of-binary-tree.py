'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        

class Solution:
    def sumBT(self, root):
        ans = 0
        
        def addtion(root):
            if root is None:
                return 0
            
            return root.data + addtion(root.left) + addtion(root.right)
            
        return addtion(root)