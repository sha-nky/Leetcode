class Solution:
    def countMajoritySubarrays(self, nums, target):
        # n = len(nums)
        # count = 0

        # for i in range(n):
        #     freq = 0

        #     for j in range(i, n):
        #         if nums[j] == target:
        #             freq += 1

        #         length = j - i + 1

        #         if freq > length // 2:
        #             count += 1

        # return count


        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] == target:
                nums[i] = 1
            else:
                nums[i] = -1

        pref = [0] * n
        pref[0] = nums[0]

        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i]

        shift = n
        freq = [0] * (2 * n + 1)

        freq[shift] = 1

        valid = 0
        lastSum = 0

        for i in range(n):
            if pref[i] > lastSum:
                valid += freq[lastSum + shift]
            else:
                valid -= freq[pref[i] + shift]

            count += valid
            freq[pref[i] + shift] += 1
            lastSum = pref[i]

        return count
