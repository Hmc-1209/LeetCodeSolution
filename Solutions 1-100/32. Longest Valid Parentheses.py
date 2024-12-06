class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * n
        maximum = 0

        for i in range(1, n):
            if s[i] == '(':
                dp[i] = 0
            elif i > 0:
                if s[i-1] == '(':
                    dp[i] = 2
                    if i > 1:
                        dp[i] += dp[i-2]
                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2
                    if i - dp[i-1] - 2 >= 0:
                        dp[i] += dp[i-dp[i-1]-2]
                maximum = max(maximum, dp[i])

        return maximum

# --- Another solution ---
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         maximum = 0
#
#         left = right = 0
#         for c in s:
#             if c == '(':
#                 left += 1
#             else:
#                 right += 1
#             if right == left:
#                 maximum = max(maximum, right * 2)
#             elif right > left:
#                 right = left = 0
#
#         left = right = 0
#         for c in reversed(s):
#             if c == '(':
#                 left += 1
#             else:
#                 right += 1
#             if right == left:
#                 maximum = max(maximum, left * 2)
#             elif left > right:
#                 right = left = 0
#
#         return maximum


s = Solution()
print(s.longestValidParentheses("(()"))
print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses(""))
print(s.longestValidParentheses("()(()"))
