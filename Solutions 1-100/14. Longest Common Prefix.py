from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = {}
        if "" in strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]

        return shortest


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
