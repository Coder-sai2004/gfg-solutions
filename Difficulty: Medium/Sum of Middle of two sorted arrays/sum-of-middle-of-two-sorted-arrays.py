class Solution:
    def findMidSum(self, arr1, arr2):
        arr1.extend(arr2)
        arr1.sort()
        n=len(arr1)//2
        return arr1[n-1]+arr1[n]