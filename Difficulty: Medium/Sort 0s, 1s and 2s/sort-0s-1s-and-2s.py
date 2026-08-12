class Solution:
    def sort012(self, arr):
        # code here
        x=arr.count(0)
        y=arr.count(1)
        z=arr.count(2)
        arr[:]=[0]*x+[1]*y+[2]*z
        return arr