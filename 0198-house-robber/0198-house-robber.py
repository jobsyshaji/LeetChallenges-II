class Solution:
    def rob(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0

        for money in nums:

            current = max(
                p1,
                p2 + money
            )

            p2 = p1
            p1 = current

        return p1