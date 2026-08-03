class Solution:
    def findSubarray(self, arr):
        pre=[arr[0]]
        d={}
        c=0
        for i in range(1,len(arr)):
            pre.append(pre[i-1]+arr[i])
            
        for i in range(len(arr)):
            
            if pre[i]==0:
                c+=1
            if (pre[i]-0) in d:
                c+=d[pre[i]-0]
            d[pre[i]]=d.get(pre[i],0)+1
            
        return c