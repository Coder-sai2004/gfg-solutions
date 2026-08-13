class Solution:
    def findUnion(self, a, b):
        # code here 
        a.extend(b)
        x=set(a)
        return sorted(list(x))