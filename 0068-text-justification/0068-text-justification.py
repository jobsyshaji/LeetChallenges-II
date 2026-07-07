class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        ans = []
        i = 0

        while i < len(words):
            j = i
            length = 0

            while j < len(words) and length + len(words[j]) + (j - i) <= maxWidth:
                length += len(words[j])
                j += 1

            gaps = j - i - 1

            if j == len(words) or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - length
                even = spaces // gaps
                extra = spaces % gaps

                line = ""
                for k in range(gaps):
                    line += words[i + k]
                    line += " " * (even + (1 if k < extra else 0))
                line += words[j - 1]

            ans.append(line)
            i = j

        return ans