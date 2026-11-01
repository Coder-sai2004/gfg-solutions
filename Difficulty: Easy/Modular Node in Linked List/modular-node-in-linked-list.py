''' Linked List Node Structure
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
'''
class Solution:
    def modularNode(self, head, k):
        ans = -1
        i = 1
        
        while head:
            if i % k == 0:
                ans = head.data
                
            i += 1
            head = head.next
        
        return ans