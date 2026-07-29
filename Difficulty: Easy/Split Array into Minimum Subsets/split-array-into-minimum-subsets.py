class Solution:
    def minSubsets(self, arr):
        arr.sort()
        c=1
        for i in range(len(arr)-1):
            if arr[i]+1!=arr[i+1]:
                c+=1
        return c