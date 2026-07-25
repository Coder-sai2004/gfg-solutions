class Solution:
    def missingNumber(self, arr):
        s=set(arr)
        n=max(arr)+1
        for i in range(1,n):
            if i not in s:
                return i
        return n