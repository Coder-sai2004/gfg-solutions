from collections import deque

class Solution:
    def dqInsertion(self, arr: list[int]) -> deque:
        ans = deque()
        for val in arr:
            ans.append(val)
        return ans