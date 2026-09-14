class Solution:
    def scores(self, a, b):
        s1=0
        s2=0
        for i in range(len(a)):
            if a[i]>b[i]:
                s1+=1
            elif b[i]>a[i]:
                s2+=1
        return [s1,s2]