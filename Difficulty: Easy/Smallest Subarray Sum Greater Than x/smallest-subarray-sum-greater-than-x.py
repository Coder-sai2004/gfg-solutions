class Solution:
    def smallestSubWithSum(self, arr , x):
        c = 0
        s = 0
        i = 0
        j = 0

        m = float('inf')

        while j < len(arr):
            s += arr[j]
            c += 1
            j += 1

            while s > x:
                m = min(m, c)
                s -= arr[i]
                i += 1
                c -= 1

        if m == float('inf'):
            return 0

        return m