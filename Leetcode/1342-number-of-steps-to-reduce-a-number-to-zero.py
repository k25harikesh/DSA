from typing import List


class Solution:
    def numberOfSteps(self, num: int) -> int:
        numberOfSteps = 0
        while (num):
            if (num % 2 == 0):
                num /= 2
                numberOfSteps += 1
            else:
                num -= 1
                numberOfSteps += 1
        return numberOfSteps


print(
    Solution().numberOfSteps(14)  # Output: 6
)
