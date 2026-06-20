class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0

        while i < len(words):
            line = []
            line_len = 0

            while (i < len(words) and
                   line_len + len(line) + len(words[i]) <= maxWidth):
                line_len += len(words[i])
                line.append(words[i])
                i += 1

            spaces = maxWidth - line_len
            gaps = len(line) - 1

            # Last line or single word
            if i == len(words) or gaps == 0:
                s = " ".join(line)
                s += " " * (maxWidth - len(s))
                res.append(s)

            else:
                even = spaces // gaps
                extra = spaces % gaps

                s = ""

                for j in range(gaps):
                    s += line[j]
                    s += " " * (even + (1 if j < extra else 0))

                s += line[-1]
                res.append(s)

        return res
        