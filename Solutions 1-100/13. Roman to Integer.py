class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        num = 0

        for i in range(len(s)):
            if i != 0 and roman[s[i]] > roman[s[i-1]]:
                num -= roman[s[i-1]] * 2
                num += roman[s[i]]
            else:
                num += roman[s[i]]

        return num


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
