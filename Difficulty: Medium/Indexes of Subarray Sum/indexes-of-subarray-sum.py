#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        if target==0:
            for i in range(len(arr)):
                if arr[i]==0:
                    return [i+1,i+1]
        i=j=s=0
        while j<len(arr)+1:
            if s<target and j<len(arr):
                s+=arr[j]
                j+=1
            elif s>target:
                s-=arr[i]
                i+=1
            else:
                break
            if s==target:
                return [i+1,j]
        return [-1]