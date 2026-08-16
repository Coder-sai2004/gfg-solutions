class Solution:
    def missingNumber(self, arr):
        # code here
        x=[]
        for i in arr:
            if i>0:
                x.append(i)
        if len(x)==0:
            return 1
        mx=max(x)
        sm=set(x)
        for i in range(1,mx+1):
            if i not in x:
                return i
        return mx+1