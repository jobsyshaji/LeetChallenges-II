class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        wordLen = len(words[0])
        totalLen = wordLen * len(words)

        target = Counter(words)

        ans = []

        for i in range(len(s) - totalLen + 1):

            seen = Counter()

            for j in range(i, i + totalLen, wordLen):
                word = s[j:j + wordLen]
                seen[word] += 1

            if seen == target:
                ans.append(i)

        return ans
        