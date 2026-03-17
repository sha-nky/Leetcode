from collections import defaultdict

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        track = defaultdict(bool)

        for bulb in bulbs:
            track[bulb] = not track[bulb]
        
        res = []
        for bulb in track:
            if track[bulb]:
                res.append(bulb)
        
        return sorted(res)
