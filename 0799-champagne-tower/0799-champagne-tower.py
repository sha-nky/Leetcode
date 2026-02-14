class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tow = [[0] * (i+1) for i in range(query_row+1)]
        tow[0][0] = poured

        for i in range(query_row):
            for j in range(len(tow[i])):
                rem = (tow[i][j] - 1) / 2.0
                if rem > 0:
                    tow[i+1][j] += rem
                    tow[i+1][j+1] += rem
        return min(1.0, tow[query_row][query_glass])
