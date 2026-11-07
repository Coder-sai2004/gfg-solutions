class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        d = set(arr)
        s = set()
        ans = []
        for ch in arr:
            if ch in d and ch not in s:
                ans.append(ch)
                s.add(ch)
            else:
                i = 1
                while ch + str(i) in d:
                    i += 1
                
                ch = ch + str(i)
                ans.append(ch)
                s.add(ch)
                d.add(ch)
                
        return ans