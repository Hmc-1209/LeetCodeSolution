class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        x = abs(x)
        result = 0

        while x > 0:
            result = result * 10 + x % 10
            x //= 10

        if result > 2 ** 31 or result < -(2 ** 31) - 1:
            return 0
        return -result if negative else result


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
