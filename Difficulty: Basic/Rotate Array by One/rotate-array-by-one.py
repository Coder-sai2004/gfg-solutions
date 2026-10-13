class Solution:
    def rotate(self, arr: list[int]) -> None:
        x = arr.pop()
        arr.insert(0,x)