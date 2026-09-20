class Solution:
    def increase(self, n, ans, target):
        if n == target:
            ans.append(n)
            return ans

        ans.append(n)
        return self.increase(n + 5, ans, target)

    def decrease(self, n, ans, target):
        if n <= 0:
            return self.increase(n, ans, target)

        ans.append(n)
        return self.decrease(n - 5, ans, target)

    def pattern(self, n):
        if n < 0:
            return [n]

        target = n
        ans = []
        return self.decrease(n, ans, target)