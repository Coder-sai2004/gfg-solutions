from collections import Counter
class Solution:
    def relativeSort(self, a1, a2):
        
        freq = Counter(a1)
        idx = 0
        
        for x in a2:
            if x in freq:
                count = freq.pop(x)
                for _ in range(count):
                    a1[idx] = x
                    idx += 1
        
        for x in sorted(freq):
            for _ in range(freq[x]):
                a1[idx] = x
                idx += 1
            