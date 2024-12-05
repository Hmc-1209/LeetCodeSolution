class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pos = len(s) - 1
        cur_l = 0

        while s[pos] == " ":
            pos -= 1

        while pos != -1 and s[pos] != " ":
            cur_l += 1
            pos -= 1

        return cur_l
