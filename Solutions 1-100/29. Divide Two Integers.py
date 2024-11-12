class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        while dividend >= divisor:
            tmpDivisor = divisor
            tmpResult = 1
            while dividend >= (tmpDivisor << 1):
                tmpDivisor <<= 1
                tmpResult <<= 1

            result += tmpResult
            dividend -= tmpDivisor

        return result if not sign else -result


s = Solution()
print(s.divide(10, 3))
print(s.divide(7, -3))
