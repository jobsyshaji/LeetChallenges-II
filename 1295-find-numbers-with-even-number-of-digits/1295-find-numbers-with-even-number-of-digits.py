class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            count = 0
            for j in str(i):
                count = count+1
            if count % 2 ==0:
                res = res+1
        return res
        
        