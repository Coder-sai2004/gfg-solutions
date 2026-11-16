class Solution:
    def findKthSmall(self, arr, k):
        l = 0
        s = set(arr)
        val = 1
        while l != k:
            if val not in s:
                val += 1
                l += 1
            else:
                val += 1
        return val - 1