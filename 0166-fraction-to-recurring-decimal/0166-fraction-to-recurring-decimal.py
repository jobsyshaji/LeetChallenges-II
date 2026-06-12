class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator % denominator == 0:
            return str(numerator // denominator)

        ans = []
        if (numerator < 0) ^ (denominator < 0):
            ans.append('-')

        numerator, denominator = abs(numerator), abs(denominator)

        ans.append(str(numerator // denominator))
        ans.append('.')

        rem = numerator % denominator
        seen = {}

        while rem:
            if rem in seen:
                ans.insert(seen[rem], '(')
                ans.append(')')
                break

            seen[rem] = len(ans)
            rem *= 10
            ans.append(str(rem // denominator))
            rem %= denominator

        return ''.join(ans)