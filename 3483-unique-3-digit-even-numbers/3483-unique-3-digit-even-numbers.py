class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)

        res = 0
        for n in range(100, 1000, 2):
            i, r = divmod(n, 100)
            j, k = divmod(r, 10)
            if freq[i] > 0:
                if freq[j] > (i == j):
                    if freq[k] > (i == k) + (j == k):
                        res += 1
        
        return res
