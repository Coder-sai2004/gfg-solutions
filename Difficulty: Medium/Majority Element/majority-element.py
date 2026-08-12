from collections import Counter
class Solution:
    def majorityElement(self, arr):
        #code here
        x=Counter(arr)
        a=0
        b=0
        for i,j in x.items():
            if a<j:
                a=j
                b=i
        if len(arr)/2<a:
            return b
        else:
            return -1