class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '':
            return not s

        start = (len(s) and p[0] in {s[0], "."})  # check if start with english or '.'

        # case start with '*' at second position
        if (len(p) >= 2) and p[1] == '*':
            return self.isMatch(s, p[2:]) or (
                        start and self.isMatch(s[1:], p))  # check x*, x -> english char with 0 or multiple times
        else:
            return start and self.isMatch(s[1:], p[1:])  # normal compare each position


s = Solution()
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("ab", ".*"))
