class Solution:
    def minimumInteger(self, arr):
        s=sum(arr)
        n=len(arr)
        arr.sort()
        for i in range(n):
            if s<=(arr[i]*n):
                return arr[i]