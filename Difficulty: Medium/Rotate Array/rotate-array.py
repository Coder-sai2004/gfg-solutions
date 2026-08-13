#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        x=[]
        y=[]
        if d>len(arr):
            i=d%len(arr)
            x=arr[i:]
            y=arr[:i]
        else:
            x=arr[d:]
            y=arr[:d]
        arr[:]=x+y
        return arr
        