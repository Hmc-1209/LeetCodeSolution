class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        start = 0
        longest = 0

        for i, c in enumerate(s):
            if c in index and index[c] >= start:
                start = index[c] + 1

            index[c] = i
            longest = max(longest, i - start + 1)

        return longest


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
