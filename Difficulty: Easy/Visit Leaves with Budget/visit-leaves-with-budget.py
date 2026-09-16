''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        if root.left is None and root.right is None:
            return 1
        res = []
        c = 1
        ans = 0
        s = 0
        i = 0

        
        def pre(node ,c):
            
            if node is None:
                return 
            
            if node.left is None and node.right is None:
                res.append(c)
                c = 0
                
            c += 1
            pre(node.left , c)
            
            pre(node.right , c)
            
        pre(root , c)
        
        
        res.sort()
        
        while i < len(res) and s + res[i] <= k:
            ans += 1
            s += res[i]
            i+=1
        
        return ans