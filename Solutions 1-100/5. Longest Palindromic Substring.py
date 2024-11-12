class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1:end]

        longest = ""
        for i in range(len(s)):
            odd_result = expand(i, i)
            even_result = expand(i, i + 1)
            if len(odd_result) > len(longest):
                longest = "".join(j for j in odd_result)
            if len(even_result) > len(longest):
                longest = "".join(j for j in even_result)
        return longest


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
