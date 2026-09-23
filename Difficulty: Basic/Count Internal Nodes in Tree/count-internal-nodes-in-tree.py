# Binary Tree Node Structure
'''class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def countNonLeafNodes(self, root):
        # add code here
        
        def leaves(root,ans):
            if root is None:
                return 0

            if root.left or root.right:
                ans = 1
            else:
                ans = 0

            left_side = leaves(root.left,ans)
            right_side = leaves(root.right,ans)

            return ans + left_side + right_side

        return leaves(root,0)