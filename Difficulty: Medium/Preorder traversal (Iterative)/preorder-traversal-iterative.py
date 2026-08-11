'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrder(self, root):
        res=[]
        def pre(root):
            if root is None:
                return
            res.append(root.data)
            pre(root.left)
            pre(root.right)
        pre(root)
        return res