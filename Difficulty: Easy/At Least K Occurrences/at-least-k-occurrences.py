class Solution:
    def firstElementKTime(self, arr,k):
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
            if d[i]==k:
                return i
        return -1