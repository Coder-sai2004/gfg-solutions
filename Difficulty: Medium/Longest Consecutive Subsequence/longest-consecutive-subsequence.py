class Solution:
    def longestConsecutive(self, arr):
        m=1
        arr.sort()
        res=0
        for i in range(1,len(arr)):
            if arr[i]-1==arr[i-1]:
                m+=1
            elif arr[i]==arr[i-1]:
                continue
            else:
                res=max(res,m)
                m=1
        res=max(res,m)
        return res