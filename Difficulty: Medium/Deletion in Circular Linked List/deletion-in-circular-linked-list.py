''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def deleteNode(self, head, key):
        tail=head
        cur=head.next
        
        while cur:
            if cur.data==key:
                tail.next=tail.next.next
                return head
            
            cur=cur.next
            tail=tail.next
            
            if cur==head and cur.data==key:
                tail.next=tail.next.next
                return tail.next
                
            elif cur==head:
                return head