class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = mn = ans = nums[0]

        for n in nums[1:]:
            if n < 0:
                mx, mn = mn, mx

            mx = max(n, mx * n)
            mn = min(n, mn * n)

            ans = max(ans, mx)

        return ans