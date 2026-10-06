class Solution:

    def countNodes(self, root):
        
        def check(root):
            if root is None:
                return 0
            
            l = check(root.left)
            r = check(root.right)
            
            return 1 + l + r
        
        return check(root)