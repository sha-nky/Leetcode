class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # counts = [0] * (max(costs) + 1)
        # for cost in costs:
        #     counts[cost] += 1
        
        # sortedCoins = []
        # for count in range(len(counts)):
        #     sortedCoins.extend([count] * counts[count])
        
        # iceCreams = 0
        # for coin in sortedCoins:
        #     if coin <= coins:
        #         iceCreams += 1
        #         coins -= coin
        #     else:
        #         return iceCreams
        
        # return iceCreams


        maxCost = max(costs)
        counts = [0] * (maxCost + 1)
        for cost in costs:
            counts[cost] += 1
        
        iceCreams = 0
        for cost in range(1, maxCost + 1):
            if counts[cost] == 0:
                continue

            canBuy = min(counts[cost], coins // cost)

            iceCreams += canBuy
            coins -= canBuy * cost

            if coins < cost:
                break

        return iceCreams
