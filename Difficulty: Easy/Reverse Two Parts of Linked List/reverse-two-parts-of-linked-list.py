""" Structure of linked list Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
"""
class Solution:
    def rever(self,head):
        if head is None or head.next is None:
            return head
        else:
            temp=head
            head=head.next
            temp.next=None
            
        while head:
            x=head.next
            head.next=temp
            temp=head
            head=x
        
        return temp
        
    def reverse(self, head, k):
        temp1=head
        temp2=head
        
        i=0
        while head:
            i+=1
            if i==k:
                temp2=head.next
                head.next=None
            head=head.next
            
        ans1=self.rever(temp1)
        ans2=self.rever(temp2)
        ans=ans1
        while ans and ans1.next:
            ans1=ans1.next
            
        ans1.next=ans2
        
        return ans
        