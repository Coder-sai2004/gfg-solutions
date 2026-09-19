class Solution:
    def count(self, n,c):
        if n < 10:
            return c
        c += 1
        
        return self.count(n//10, c)
    def countDigits(self, n):
        c = 1
        return self.count(n,c)