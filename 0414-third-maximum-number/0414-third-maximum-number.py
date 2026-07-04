class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))


        if len(nums) < 3:
            return max(nums)
        first_max = max(nums)
        nums.remove(first_max)
        s_max = max(nums)
        nums.remove(s_max)
        t_max = max(nums)
        return t_max