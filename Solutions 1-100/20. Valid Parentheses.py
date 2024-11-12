class Solution:
    def isValid(self, s: str) -> bool:
        openParens = ["(", "[", "{"]
        closeParens = [")", "]", "}"]
        stack = []

        for c in s:
            if c in openParens:
                stack.append(c)
            else:
                if not stack or stack.pop() != openParens[closeParens.index(c)]:
                    return False

        if stack != []:
            return False

        return True


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))
