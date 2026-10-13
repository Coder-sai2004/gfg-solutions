'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def hasPathSum(self, root, target):
        def check(node,t,s):
            if node is None:
                return

            if node.left is None and node.right is None:
                s += node.data
                if s == t:
                    return True


            l = check(node.left,t,s + node.data)
            r = check(node.right,t,s + node.data)

            if l or r:
                return True
            return False

        if root is None:
            return False
        return check(root,target,0)
