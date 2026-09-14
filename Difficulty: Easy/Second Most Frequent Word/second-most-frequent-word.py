from collections import Counter
class Solution:
    def secFrequent(self, arr):
        d=Counter(arr)
        val=sorted(set(d.values()),reverse=True)
        
        if len(val)<2:
            return -1
        else:
            return val[1]