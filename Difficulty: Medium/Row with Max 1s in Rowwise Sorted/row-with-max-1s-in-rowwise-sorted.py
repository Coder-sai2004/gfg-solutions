class Solution:
    def rowWithMax1s(self, arr):
        # code here
        x=0
        y=0
        z=0
        for sub in range(len(arr)):
            x=arr[sub].count(1)
            if z<x:
                y=sub
                z=x
        if z>0:
            return y
        else:
            return -1