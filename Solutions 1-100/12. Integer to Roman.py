class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        digits = []
        currentBase = 10 ** (len(str(num)) - 1)

        i = 0
        while int(num) > 0:
            if num % 10 != 0:
                digits.insert(0, (num % 10) * (10 ** i))
            else:
                digits.insert(0, 0)
            num //= 10
            i += 1

        i = 0
        while i < len(digits):
            currentValue = int(digits[i] / currentBase)
            if currentValue == 0:
                currentBase //= 10
                i += 1
                continue
            if currentValue >= 5 and currentValue < 9:
                digits[i] = (currentValue - (currentValue - 5)) * currentBase
                for j in range(i, i + currentValue - 5):
                    digits.insert(j + 1, currentBase)
                    i += 1
            elif currentValue == 9:
                digits[i] = currentBase * 10
                digits.insert(i, currentBase)
                i += 1
            elif currentValue == 4:
                digits[i] = 5 * currentBase
                digits.insert(i, currentBase)
                i += 1
            elif currentBase != 0:
                digits[i] = currentBase
                for j in range(currentValue - 1):
                    digits.insert(i, currentBase)
                    i += 1
            currentBase //= 10
            i += 1

        print(digits)
        return "".join(roman[c] for c in digits if c != 0)


s = Solution()
print(s.intToRoman(3749))
print(s.intToRoman(58))
print(s.intToRoman(1994))
