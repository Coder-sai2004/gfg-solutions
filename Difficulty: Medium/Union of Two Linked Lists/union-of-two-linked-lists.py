""" Linked List Node Structure
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

"""
class Solution:
    def makeUnion(self, head1, head2):
        s = set()
        head = None
        tail = None
        
        while head1:
            
            if head1.data not in s:
                
                s.add(head1.data)
                node = Node(head1.data)
                
                if head is None:
                    head = node
                    tail = node
                else:
                    tail.next = node
                    tail = node
            
            head1 = head1.next
                    
        
        while head2:
            
            if head2.data not in s:
                
                s.add(head2.data)
                node = Node(head2.data)
                
                if head is None:
                    head = node
                    tail = node
                else:
                    tail.next = node
                    tail = node
                    
            head2 = head2.next
                    
        
        return head