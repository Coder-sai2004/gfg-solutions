from collections import deque 
class kQueues:

    def __init__(self, n, k):
        # Initialize your data members
        self.arr=[deque([]) for _ in range(k)]
        self.n=n
        
    def enqueue(self, x, i):
        # Enqueue element x into queue number i
        self.arr[i].append(x)

    def dequeue(self, i):
        # Dequeue element from queue number i
        if len(self.arr[i])==0:
            return -1
        return self.arr[i].popleft()

    def isEmpty(self, i):
        # Check if queue i is empty
        if len(self.arr[i])>0:
            return False
        return True
        
        
    def isFull(self):
        # Check if array is full
        size=sum(len(x) for x in self.arr)
        if size<self.n:
            return False
        return True