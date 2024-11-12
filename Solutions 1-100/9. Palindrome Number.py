class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        reverse = 0
        if x < 0:
            return False

        while y > 0:
            reverse = reverse * 10 + y % 10
            y //= 10
        return True if reverse == x else False


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
