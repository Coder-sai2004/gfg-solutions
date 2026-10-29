''' Structure of Linked List Node
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
class Solution:
    def flatten(self, head):
        values = []
        new_head = None
        tail = None

        def traverse(node):
            if node is None:
                return

            # Store the current node's value
            values.append(node.data)

            # Traverse the child list first
            if node.bottom is not None:
                traverse(node.bottom)

            # Continue with the next node
            node = node.next
            traverse(node)

        traverse(head)
        
        values.sort()
        
        # Create a new flattened doubly linked list
        for value in values:
            new_node = Node(value)

            if new_head is None:
                new_head = new_node
                tail = new_node
            else:
                tail.bottom = new_node
                tail = new_node

        return new_head