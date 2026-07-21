'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def compare(self, head1, head2):
        s1=''
        s2=''
        while head1:
            s1+=head1.data
            head1=head1.next
        while head2:
            s2+=head2.data
            head2=head2.next
        
        if s1==s2:
            return 0
        elif s1>s2:
            return 1
        else:
            return -1