class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        length = 0

        for char in s:
            if char == '*':
                length = max(0, length - 1)
            elif char == '#':
                length *= 2
            elif char == '%':
                pass
            else:
                length += 1

            lengths.append(length)

        if k >= length:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            L = lengths[i]

            if char.isalpha():
                if k == L - 1:
                    return char

            elif char == '#':
                half = L // 2
                k %= half

            elif char == '%':
                k = L - 1 - k

            elif char == '*':
                pass

        return '.'
