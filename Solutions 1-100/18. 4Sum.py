from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()

        def kSum(start, target, k):
            result = []
            if k == 2:
                i, j = start, len(nums) - 1
                while i < j:
                    current_result = nums[i] + nums[j]
                    if current_result == target:
                        result.append([nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1
                    elif current_result < target:
                        i += 1
                    else:
                        j -= 1
                return result

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                for subResult in kSum(i + 1, target - nums[i], k - 1):
                    result.append([nums[i]] + subResult)

            return result

        return kSum(0, target, 4)


s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
print(s.fourSum([2,2,2,2,2], 8))
