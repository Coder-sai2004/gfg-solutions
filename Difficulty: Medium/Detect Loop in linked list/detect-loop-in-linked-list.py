'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        slow=head
        fast=head
        while slow:
            slow=slow.next
            if fast.next is None or fast.next.next is None:
                return False
            fast=fast.next.next
            if slow==fast:
                return True
        
