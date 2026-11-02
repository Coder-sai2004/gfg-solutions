''' Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def modifyTheList(self, head):
        count = 0
        values = []

        current = head
        node = head

        # Store all node values and count the nodes
        while current:
            count += 1
            values.append(current.data)
            current = current.next

        middle = count // 2

        left = 0
        right = count - 1

        # Update the linked list using values from both ends
        while node:
            if left < middle:
                node.data = values[right] - values[left]
                left += 1
                right -= 1
            else:
                node.data = values[right]
                right -= 1

            node = node.next

        return head