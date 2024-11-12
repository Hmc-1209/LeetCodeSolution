class Solution:
    def convert(self, s: str, numRows: int) -> str:

        r = 0
        rows = [""] * numRows
        slide = True

        for chr in s:
            rows[r] += chr
            if numRows != 1 and (r == numRows - 1 or r == 0):
                slide = not slide
            if numRows != 1:
                r += -1 if slide else 1

        result = "".join(string for string in rows)

        return result


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
print(s.convert("A", 1))
