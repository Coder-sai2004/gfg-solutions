# Structure of a Tree Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def treePathsSum(self, root):
        res = []
        def check(root,ans):
            if root is None:
                return 
            
            ans += str(root.data)
            
            if root.left is None and root.right is None:
                res.append(int(ans))
                
            check(root.left,ans)
            check(root.right,ans)
            
        check(root,"")
        
        return sum(res)