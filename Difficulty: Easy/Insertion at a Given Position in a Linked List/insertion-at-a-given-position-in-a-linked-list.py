'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
        node=Node(val)
        if pos==1:
            node.next=head
            return node
        temp=head
        i=0
        while head:
            i+=1
            if i+1==pos:
                x=head.next
                head.next=None
                break
            head=head.next
        head.next=node
        node.next=x
        return temp