class Solution:
    def sortIt(self, arr):
        odd=[]
        even=[]
        for i in arr:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        arr[:]=sorted(odd)[::-1]+sorted(even)