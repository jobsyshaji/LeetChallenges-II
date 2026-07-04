class Solution:
    def findLucky(self, arr: List[int]) -> int:
      
        freq = {}

        for i in arr:
            freq[i] = freq.get(i, 0) + 1

        lucky = []

        for i in freq:
            if i == freq[i]:
                lucky.append(i)

        if lucky:
            return max(lucky)

        return -1
    
