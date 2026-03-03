class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        totalSum = sum(nums)

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        largest = -float("inf")
        for num in freq:
            potential = totalSum - 2*num
            if potential in freq:
                if potential != num or freq[num] > 1:
                    largest = max(largest, potential)
        
        return largest
