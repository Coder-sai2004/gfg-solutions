'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def printList(self, head):
        res = []
        while head:
            res.append(head.data)
            head = head.next
        return res