class Solution:
    def findSubString(self, s):
        unique_chars = len(set(s))
        min_length = float('inf')
        freq = {}
        left = 0
        right = 0

        # Expand the window
        while right < len(s):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1

            # Shrink while all characters are present
            while len(freq) == unique_chars:
                min_length = min(min_length, right - left + 1)

                if freq[s[left]] == 1:
                    del freq[s[left]]
                else:
                    freq[s[left]] -= 1

                left += 1

            right += 1

        return min_length