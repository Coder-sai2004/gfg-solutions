class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        maxc=maxg=arr[0]
        for i in range(1,len(arr)):
            maxc=max(arr[i],maxc+arr[i])
            if maxc>maxg:
                maxg=maxc
        return maxg