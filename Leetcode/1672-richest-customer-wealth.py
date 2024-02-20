from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        L = []

        for acc in accounts:
            L.append(sum(acc))

        # print(L)
        return max(L)


print(
    Solution().maximumWealth(
        [[1, 2, 3], [3, 2, 1]]
    )  # Output: 6
)
