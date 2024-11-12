from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = 0
        n2 = 0
        nums3 = []
        total_len = len(nums1) + len(nums2)
        for i in range(total_len):
            if (n2 >= len(nums2) or (n1 < len(nums1) and nums1[n1] < nums2[n2])):
                nums3.append(nums1[n1])
                n1 += 1
            else:
                nums3.append(nums2[n2])
                n2 += 1

        if total_len % 2 == 0:
            return (nums3[int(total_len / 2 - 1)] + (nums3[int(total_len / 2)])) / 2
        else:
            return nums3[int(total_len / 2)]


s = Solution()
print(s.findMedianSortedArrays([1,3], [2]))
print(s.findMedianSortedArrays([1,2], [3,4]))
