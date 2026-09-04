class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        track = defaultdict(list)
        n = len(nums)

        if n == 1:
            return 0 if (0 <= k) else -1

        maximum, minimum = nums[0], nums[0]
        for i in range(n):
            track[i].append(maximum)
            maximum = max(maximum, nums[i])
            minimum = nums[i]

            for j in range(i, n):
                minimum = min(minimum, nums[j])
        
            track[i].append(minimum)
        
        for i in track.keys():
            maximum, minimum = track[i]
            if maximum - minimum <= k:
                return i
        
        return -1
