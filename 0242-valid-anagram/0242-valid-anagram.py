class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        for i in s:
            s_freq[i] = s_freq.get(i, 0)+1
        t_freq = {}
        for j in t:
            t_freq[j]= t_freq.get(j, 0)+1
        return s_freq == t_freq
            

        