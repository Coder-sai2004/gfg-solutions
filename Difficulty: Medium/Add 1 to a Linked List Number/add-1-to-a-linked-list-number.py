''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def reverse(self,head):
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
    def addOne(self,head):
        #reverse the linked list first
        temp=self.reverse(head)
        res=temp
        carry=1
        while temp:
            #if temp.data value is less than 9 then we just need to add one to the value
            #and break the loop so there is no need of carry.
            if temp.data<9:
                temp.data+=carry
                carry-=1
                break
            #if value is 9 then after adding one it becomes 10
            #so we need to add carry to next node
            else:
                x=temp.data+carry
                carry-=1
                temp.data=x%10
                carry=x//10
                
            #if we have carry left ,then create a new node and link it.
            #we will add one in that node in next iteration
            if temp.next is None and carry==1:
                node=Node(0)
                temp.next=node
                
            temp=temp.next
        #reverse the linked list to get the required result
        ans=self.reverse(res)
        return ans