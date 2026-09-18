'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
        if root is None or (root.left is None and root.right is None):
            return 0
            
        
        res = []
        ans = float('inf')
        
        def pre(node):
            if node is None:
                return 
            
            pre(node.left)
            res.append(node.data)
            pre(node.right)
        
        
        pre(root)
        
        res.sort()
        
        for i in range(1,len(res)):
            ans = min(ans, (res[i]-res[i-1]))
            
        return ans