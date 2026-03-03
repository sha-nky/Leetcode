class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        largest = -1
        for num in freq:
            if freq[num] == num:
                largest = max(largest, num)
        return largest
