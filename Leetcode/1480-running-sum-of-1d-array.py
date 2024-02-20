from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = 0
        for i in range(len(nums)):
            a += nums[i]
            nums[i] = a
        return nums


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # results = list(nums)
        results = [nums[0]] * len(nums)

        # print(results)

        for i in range(1, len(nums)):
            results[i] = nums[i] + results[i - 1]
            # print(i, results)
        return nums


print(
    Solution().runningSum([1, 2, 3, 4])  # Output: [1,3,6,10]
)
