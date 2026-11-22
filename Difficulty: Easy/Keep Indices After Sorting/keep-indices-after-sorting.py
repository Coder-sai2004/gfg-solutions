from collections import defaultdict
class Solution:
    def sortWithIndices(self, arr: list[int]) -> list[list[int]]:
        s = set(arr)
        s = sorted(s)
        res = []
        d = defaultdict(list)
        
        for i in range(len(arr)):
            d[arr[i]].append(i)
        
        for num in s:
            temp = d[num]
            
            if len(temp) == 1:
                res.append([ num, temp[0] ])
            else:
                i = 0
                while i < len(temp):
                    res.append([ num, temp[i] ])
                    i += 1
                    
        return res