# structure of a binary tree node
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''
class Solution:
    def maxPathSum(self, root):
        # code here
        def check(node,s):
            if node is None:
                return -1000000

            if node.left is None and node.right is None:
                s += node.data
                return s


            l = check(node.left,s + node.data)
            r = check(node.right,s + node.data)

            return max(l,r)

        if root is None:
            return 0
        return check(root,0)