''' Linked List Node Structure
class NodeLL:
    def __init__(self, data):
        self.data = data
        self.next = None


Binary Tree Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
class Solution:
    def linkedListToBinaryTree(self, head):
        if head is None:
            return None
            
        root = Node(head.data)
        
        queue = [root]
        
        head = head.next
        
        while head:
            temp = queue.pop(0)
            
            temp.left = Node(head.data)
            queue.append(temp.left)
            head = head.next
            
            if head:
                temp.right = Node(head.data)
                queue.append(temp.right)
                head = head.next
        return root