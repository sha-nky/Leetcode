class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = [0] * (max(costs) + 1)
        for cost in costs:
            counts[cost] += 1
        
        sortedCoins = []
        for count in range(len(counts)):
            sortedCoins.extend([count] * counts[count])
        
        iceCreams = 0
        for coin in sortedCoins:
            if coin <= coins:
                iceCreams += 1
                coins -= coin
            else:
                return iceCreams
        
        return iceCreams
