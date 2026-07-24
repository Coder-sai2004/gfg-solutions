class Solution:

    def modifyArray(self, arr):
        n=len(arr)
        res=[]
        s=set(arr)
        for i in range(n):
            if i in s:
                res.append(i)
            else:
                res.append(-1)
        arr[:]=res
        return arr