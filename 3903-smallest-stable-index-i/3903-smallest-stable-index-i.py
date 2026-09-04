class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # track = defaultdict(list)
        # n = len(nums)

        # if n == 1:
        #     return 0 if (0 <= k) else -1

        # maximum, minimum = nums[0], nums[0]
        # for i in range(n):
        #     track[i].append(maximum)
        #     maximum = max(maximum, nums[i])
        #     minimum = nums[i]

        #     for j in range(i, n):
        #         minimum = min(minimum, nums[j])
        
        #     track[i].append(minimum)
        
        # for i in track.keys():
        #     maximum, minimum = track[i]
        #     if maximum - minimum <= k:
        #         return i
        
        # return -1


        n = len(nums)

        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        prefix_max = nums[0]

        for i in range(n):
            if prefix_max - suffix_min[i] <= k:
                return i

            prefix_max = max(prefix_max, nums[i])

        return -1
