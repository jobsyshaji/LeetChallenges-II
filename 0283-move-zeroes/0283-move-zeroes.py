class Solution(object):
    def moveZeroes(self, nums):
 
        moved = []
        for i in nums:
            if i != 0:
                moved.append(i)
        x = len(nums)
        y = len(moved)
        z = x - y

        for _ in range(z):
            moved.append(0)
        nums[:] = moved
     



       
        