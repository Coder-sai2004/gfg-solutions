from collections import Counter
class Solution:
    def getMaxOccuringChar(self, s):
        #calculating frequencies
        x=Counter(s)
        #initializing the maximum value
        m=max(x.values())
        res=[]
        #assigning the characters which have max frequency
        for i,j in x.items():
            if j==m:
                res.append(i)
        #returning the lexicographically smallest character which has highest frequency
        res.sort()
        return res[0]