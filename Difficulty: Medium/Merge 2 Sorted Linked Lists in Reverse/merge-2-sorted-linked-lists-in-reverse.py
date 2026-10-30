'''Structure for linked list Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''
class Solution:
    
    def reverseList(self, head):
        if head and head.next:
            tail=head
            head=head.next
            tail.next=None
        else:
            return head
        while head:
            x=head.next
            head.next=tail
            tail=head
            head=x
        
        return tail
    
    def mergeResult(self, head1, head2):
        head = None
        tail = None
        rev = None
        
        while head1 and head2:
            if head1.data < head2.data:
                node = head1
                head1 = head1.next
                node.next = None
                
            else:
                node = head2
                head2 = head2.next
                node.next = None
            
            if head is None:
                head = node
                tail = node
            else:
                rev = node
                tail.next = rev
                rev.next = tail
                tail = rev
                
        if head1:
            tail.next = head1
        
        if head2:
            tail.next = head2
                
        return self.reverseList(head)