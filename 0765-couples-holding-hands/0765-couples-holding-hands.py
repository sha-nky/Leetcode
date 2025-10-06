class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        swaps = 0
        pos = {person: i for i, person in enumerate(row)}
        n = len(row)
        
        for i in range(0, n, 2):
            curr = row[i]
            partner = curr ^ 1

            if row[i+1] != partner:
                swaps += 1
                partner_pos = pos[partner]
                neighbour = row[i+1]
                row[i+1], row[partner_pos] = row[partner_pos], row[i+1]

                pos[neighbour] = partner_pos
                pos[partner] = i+1
        
        return swaps
