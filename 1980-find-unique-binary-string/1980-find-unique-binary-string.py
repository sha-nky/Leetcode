class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = [int(x, 2) for x in nums]
        n = len(nums)

        for num in range(2**n):
            if num not in nums:
                binary = bin(num)[2:]
                zeroes = n - len(binary)
                return zeroes * "0" + binary
        
        return None
