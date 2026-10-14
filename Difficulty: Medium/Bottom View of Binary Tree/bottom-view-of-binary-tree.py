'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
class Solution:
    def bottomView(self, root):
        bottom_nodes = {}

        def traverse(root, pos, depth):
            if root is None:
                return 

            # Update the bottommost node at each position
            if pos in bottom_nodes:
                if depth >= bottom_nodes[pos][0]:
                    bottom_nodes[pos] = [depth, root.data]
            else:
                bottom_nodes[pos] = [depth, root.data]

            traverse(root.left, pos - 1, depth + 1)
            traverse(root.right, pos + 1, depth + 1)

        traverse(root, 0, 0)

        result = []
        sorted_positions = sorted(bottom_nodes.keys())
        for k in sorted_positions:
            result.append(bottom_nodes[k][1])

        return result