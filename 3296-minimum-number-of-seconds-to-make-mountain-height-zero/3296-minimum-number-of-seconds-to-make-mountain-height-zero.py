class Solution:
    def minNumberOfSeconds(self, height: int, times: list[int]) -> int:
        l, h = 1, 10**16

        while l < h:
            mid = (l + h) >> 1
            tot = 0
            for t in times:
                tot += int(math.sqrt(mid / t * 2 + 0.25) - 0.5)
                if tot >= height: break
            if tot >= height:
                h = mid
            else:
                l = mid + 1

        return l
