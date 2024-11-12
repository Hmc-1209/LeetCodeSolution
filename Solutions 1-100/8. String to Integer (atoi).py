class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        sign = None
        start = False
        result = 0

        if (s == "" or s == "+" or s == "-") or (s[0] not in "+-0123456789"):
            return 0

        for i in range(len(s)):
            if (not start) and (s[i] in "+-"):
                if sign != None:
                    return 0
                sign = True if s[i] == "+" else False
            elif s[i] in "0123456789":
                result = result * 10 + int(s[i])
                start = True
            else:
                break

        result = -result if sign == False else result

        if sign == False and result < -(2 ** 31):
            result = -(2 ** 31)
        elif result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        return result


s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("-042"))
print(s.myAtoi("1337c0d3"))
print(s.myAtoi("0-1"))
print(s.myAtoi("words and 987"))
