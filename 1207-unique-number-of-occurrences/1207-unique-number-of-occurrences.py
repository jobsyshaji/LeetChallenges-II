class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i,0)+ 1
        ans = list(freq.values())
        return len(ans) == len(set(ans))
        

