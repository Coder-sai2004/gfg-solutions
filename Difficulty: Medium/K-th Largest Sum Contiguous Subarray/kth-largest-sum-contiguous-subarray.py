from typing import List


class Solution:
    def kthLargest(self, arr, k) -> int:
        res=[]
        pre=[arr[0]]
        
        for i in range(1,len(arr)):
            pre.append(pre[i-1]+arr[i])
        
        for i in range(len(pre)):
            for j in range(i):
                res.append(pre[i]-pre[j])
        
        ans=sorted(pre+res,reverse=True)
        
        return ans[k-1]