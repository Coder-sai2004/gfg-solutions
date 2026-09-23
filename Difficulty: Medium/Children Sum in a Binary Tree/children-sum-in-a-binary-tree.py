'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        
        def check(root):
            if root is None:
                return 
            
            if root.left and root.right:
                if root.left.data + root.right.data != root.data:
                    return False
                    
            elif root.left and root.left.data != root.data:
                    return False
                    
            elif root.right and root.right.data != root.data:
                    return False
            
            l = check(root.left)
            r = check(root.right)
            
            if l is False or r is False:
                return False
        
        if check(root) == None:
            return True
        return False