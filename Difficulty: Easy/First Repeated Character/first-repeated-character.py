class Solution:
    def firstRepChar(self, s):
        t=set()
        for ch in s:
            if ch in t:
                return ch
            else:
                t.add(ch)
        return -1