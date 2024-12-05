from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def findCombination(targetRemain, currentCombination, startPos):
            if targetRemain == 0:
                ans.append(list(currentCombination))
                return

            if targetRemain < 0:
                return

            for i in range(startPos, len(candidates)):
                currentCombination.append(candidates[i])
                findCombination(targetRemain - candidates[i], currentCombination, i)
                currentCombination.pop()

        findCombination(target, [], 0)
        return ans


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
