class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = max(nums)
        maxi_index = nums.index(maxi)
        for i in range(len(nums)):
            if i != maxi_index:
                if maxi < 2 * nums[i]:
                    return -1
        
        return maxi_index
        

        