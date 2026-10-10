# A Tree node
# struct Node
# {
#     int key;
#     struct Node *left, *right;
# };
class Solution:
    def printPaths(self, root, s):
        res = []
        temp = []

        def check(node,t):
            if node is None:
                return

            temp.append(node.data)

            if sum(temp) == t:
                res.append(temp.copy())

            check(node.left,t)
            check(node.right,t)
            temp.pop()

        check(root,s)
        return res