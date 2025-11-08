class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high, ans = 1, max(piles), max(piles)
        
        while low<=high:
            mid = (low+high)//2

            time_needed = sum(math.ceil(pile / mid) for pile in piles)
            if time_needed <= h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans