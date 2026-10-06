''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def levelOrder(self, root):
        q = deque([])
        res = []
        q.append(root)
        
        while q:
            x = q.popleft()
            res.append(x.data)
            
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        
        return res