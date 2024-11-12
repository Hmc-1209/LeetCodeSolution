from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximumArea = 0
        start = 0
        end = len(height) - 1

        while (start < end):
            currentArea = height[start] * (end - start) if height[start] < height[end] else height[end] * (end - start)
            if currentArea > maximumArea:
                maximumArea = currentArea
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return maximumArea


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
