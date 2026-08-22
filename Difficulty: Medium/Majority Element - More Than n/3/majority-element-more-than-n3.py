from collections import Counter
class Solution:
    def findMajority(self, arr):
        freq=Counter(arr)
        target=len(arr)//3
        res=[]
        for key,val in freq.items():
            if val>target:
                res.append(key)
        res.sort()
        if res:
            return res
        return []