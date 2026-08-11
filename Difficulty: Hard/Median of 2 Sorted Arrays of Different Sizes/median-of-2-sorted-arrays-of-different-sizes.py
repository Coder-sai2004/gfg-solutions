class Solution:
    def medianOf2(self, a, b):
        a.extend(b)
        a=sorted(a)
        m=len(a)//2
        if len(a)%2!=0:
            return a[m]
        return (a[m]+a[m-1])/2