class Solution(object):
    def permute(self, nums):
        res = []

        def bt(path, rem):
            if not rem:
                res.append(path)
                return
            for i in range(len(rem)):
                bt(path + [rem[i]], rem[:i] + rem[i+1:])

        bt([], nums)
        return res
        