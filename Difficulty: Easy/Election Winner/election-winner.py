from collections import Counter
class Solution:
    def winner(self, arr):
        res=Counter(arr)
        mx=max(res.values())
        temp=[]
        for key,val in res.items():
            if val==mx:
                temp.append(key)
        temp.sort()
        return temp[0],res[temp[0]]