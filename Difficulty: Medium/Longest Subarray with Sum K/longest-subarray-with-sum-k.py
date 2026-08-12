class Solution:
    def longestSubarray(self, arr, k):  
        res=0
        pre=[arr[0]]
        s={}
        s[0]=0
        
        
        for i in range(1,len(arr)):
            pre.append(arr[i]+pre[i-1])
                
                
        for i in range(len(pre)):
            x=pre[i]-k

            if pre[i]>=k and abs(x) in s:
                res=max(res,(i+1)-s[x])

            elif pre[i]<k and x in s:
                res=max(res,(i+1)-s[x])
                
            if pre[i] in s:
                continue
            else:
                s[pre[i]]=i+1
        return res