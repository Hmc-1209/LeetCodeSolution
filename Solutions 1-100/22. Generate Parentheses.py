from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dp(current, openParen, closeParen):
            if len(current) == n * 2:
                result.append(current)

            if openParen < n:
                dp(current + '(', openParen + 1, closeParen)

            if closeParen < openParen:
                dp(current + ')', openParen, closeParen + 1)

            return result

        return dp("", 0, 0)


s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(1))
