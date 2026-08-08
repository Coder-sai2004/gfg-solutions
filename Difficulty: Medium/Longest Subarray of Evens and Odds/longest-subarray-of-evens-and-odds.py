class Solution:
    def maxEvenOdd(self, arr):
        ans=0
        c=1
        x=0
        y=0
        if arr[0]%2==0:
            x=0
        else:
            x=1
        for i in range(1,len(arr)):
            if arr[i]%2==0:
                y=0
            else:
                y=1
                
            if x!=y:
                c+=1
                x=y
            else:
                ans=max(ans,c)
                c=1
        
        ans=max(ans,c)
        
        return ans