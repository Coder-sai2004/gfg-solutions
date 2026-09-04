class Solution:
    def getDistinctDifference(self, arr: list[int]) -> list[int]:
        #ans is for final result, s1 and s2 used to track distinct integers from left and right side
        #left and right are used to store dinstict integers present at the time of inserting
        ans=[]
        s1 = set()
        s2 = set()
        left = []
        right = []
        
        #c1 and c2 keep the count of distinct integers at the current index from both left ad right sides
        c1 = 0
        c2 = 0
        n = len(arr)
        
        #finding distinct integers from both ends of the current index
        for i in range(n):
            if arr[i] not in s1:
                s1.add(arr[i])
                c1 += 1
            left.append(c1)
            
            if arr[n-i-1] not in s2:
                s2.add(arr[n-i-1])
                c2 += 1
            right.append(c2)
        
        right = right[::-1]
        
        #calculation of distinct difference at every index
        for i in range(n):
            l = left[i-1] if i-1 > -1 else 0
            r = right[i+1] if i+1 < n else 0
            ans.append(l-r)
        
        return ans