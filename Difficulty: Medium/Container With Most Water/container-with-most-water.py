class Solution:
    def maxWater(self, arr):
        max_area=total_area=0
        i=0
        j=len(arr)-1
        while i<j:
            total_area=min(arr[i],arr[j])*(j-i)
            max_area=max(max_area,total_area)
            if arr[i]<arr[j]:
                i+=1
            else:
                j-=1
        return max_area