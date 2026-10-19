"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def printList(self, head):
        while head:
            print(head.data,end = " ")
            head = head.next