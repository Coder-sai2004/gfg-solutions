from collections import Counter
class Solution:
    def countArray(self, arr, x):
        res=[]
        d=Counter(arr)
        for i in arr:
            res.append(d[(i+x)//2])
        return res