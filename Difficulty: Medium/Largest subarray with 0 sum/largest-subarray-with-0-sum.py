class Solution:
    def maxLength(self, arr):
        res=0
        pre=[arr[0]]
        s={}
        s[0]=0
        
        
        for i in range(1,len(arr)):
            pre.append(arr[i]+pre[i-1])
                
                
        for i in range(len(pre)):
            x=pre[i]-0

            if pre[i]>=0 and abs(x) in s:
                res=max(res,(i+1)-s[x])

            elif pre[i]<0 and x in s:
                res=max(res,(i+1)-s[x])
                
            if pre[i] in s:
                continue
            else:
                s[pre[i]]=i+1
        return res