class Solution(object):
    def restoreIpAddresses(self, s):

        ans = []

        def dfs(i, parts):
            if len(parts) == 4:
                if i == len(s):
                    ans.append(".".join(parts))
                return

            for j in range(i, min(i + 3, len(s))):
                part = s[i:j + 1]

                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue

                dfs(j + 1, parts + [part])

        dfs(0, [])
        return ans
        