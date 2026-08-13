class Solution:
    def kthSmallest(self, arr, k):
        x=sorted(arr)
        return x[k-1]
        
