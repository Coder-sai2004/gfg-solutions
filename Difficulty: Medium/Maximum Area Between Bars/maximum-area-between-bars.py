class Solution:
    def maxArea(self, height):
        i=0
        j=len(height)-1
        area=0
        while i<j:
            h=min(height[i],height[j])
            w=j-i-1
            area=max(area,(h*w))
            
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area