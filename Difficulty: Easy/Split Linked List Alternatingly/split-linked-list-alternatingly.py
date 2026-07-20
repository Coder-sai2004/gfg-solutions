'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #single node edge case
        if head.next is None:
            return head,None
            
        #one,two is for iterating and first,second is for returning the answer
        one=head
        two=head.next
        first=one
        second=two
        #calculating the size of the linkedlist
        n=0
        while head:
            n+=1
            head=head.next
        #generating the alternating lists
        while one and one.next and two and two.next:
            one.next=one.next.next
            one=one.next
            
            two.next=two.next.next
            two=two.next
            
        #if the size is even then remove the last node from one
        if n%2==0:
            one.next=None

        return first,second