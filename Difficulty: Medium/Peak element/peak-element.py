class Solution:   
    def peakElement(self, arr):
        # Code here
        if len(arr)==1:
            return 0
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return i
            elif arr[len(arr)-2]<arr[len(arr)-1]:
                return len(arr)-1
            elif arr[i]<arr[i+1]>arr[i+2]:
                return i+1
        return -1