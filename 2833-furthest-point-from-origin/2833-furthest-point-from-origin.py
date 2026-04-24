class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dist = 0
        n = len(moves)
        count = 0

        for i in range(n):
            if moves[i] == "L":
                dist -= 1
            elif moves[i] == "R":
                dist += 1
            else:
                count += 1
        
        return dist + count if dist >= 0 else abs(dist - count)
