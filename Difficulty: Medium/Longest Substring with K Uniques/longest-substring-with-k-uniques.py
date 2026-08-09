class Solution:
    def longestKSubstr(self, s, k):
        # freq stores the frequency of each character in the current window.
        # left and right are the sliding window pointers.
        # distinct stores the number of distinct characters in the current window.
        # cur_max stores the current window length.
        # ans stores the maximum length of a substring with exactly k distinct characters.

        freq = {}
        left = 0
        right = 0
        distinct = 0
        cur_max = 0
        ans = -1

        while right < len(s):
            # If the current window has exactly k distinct characters,
            # update the answer.
            if distinct == k:
                ans = max(ans, cur_max)

            # If the window already has k distinct characters and a new
            # character appears, shrink the window until one distinct
            # character is removed.
            if s[right] not in freq and distinct == k:
                while distinct == k:
                    if freq[s[left]] == 1:
                        del freq[s[left]]
                        distinct -= 1
                    else:
                        freq[s[left]] -= 1

                    cur_max -= 1
                    left += 1

                # Add the new character after removing one distinct character.
                freq[s[right]] = 1
                distinct += 1

            # If the character already exists in the window,
            # increase its frequency.
            elif s[right] in freq:
                freq[s[right]] += 1

            # If the character is new and the window has fewer than
            # k distinct characters, add it to the window.
            else:
                freq[s[right]] = 1
                distinct += 1

            # Expand the window.
            cur_max += 1
            right += 1

        # Final check for the last window.
        if distinct == k:
            ans = max(ans, cur_max)

        return ans