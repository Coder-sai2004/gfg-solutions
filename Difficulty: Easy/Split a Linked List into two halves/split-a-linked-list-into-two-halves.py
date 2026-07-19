'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''


class Solution:
    def splitList(self, head):
        slow=head
        fast=head
        n=0
        #calculating the size of linked list
        while fast.next:
            slow=slow.next
            fast=fast.next.next
            n+=1
            if slow==fast:
                break
        #finding the middle node
        if n%2==0:
            m=n//2
        else:
            m=(n//2)+1
        c=0
        while slow.next:
            c+=1
            #if middle node found break it into two halves
            if c==m:
                fast=slow.next
                slow.next=head
                slow=fast
                c+=1
            if c==n:
                slow.next=fast
                break
            slow=slow.next
        return head,fast