''' Structure of Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def reverseLevelOrder(self, root):
        res = []
        ans = []
        
        def order(root,level,res):
            if root is None:
                return 
        
            if len(res) <= level:
                res.append([])
        
            res[level].append(root.data)
        
            order(root.left,level + 1,res)
            order(root.right,level + 1,res)
        
        order(root,0,res)
        res = res[::-1]
        
        for sub in res:
            ans.extend(sub)
            
        return ans