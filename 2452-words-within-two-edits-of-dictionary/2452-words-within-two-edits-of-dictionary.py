class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def isPossible(x, y):
            count = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    count += 1
            
            return True if count <= 2 else False
        
        res = [0]

        for i in range(len(queries)):
            for j in range(len(dictionary)):
                if isPossible(queries[i], dictionary[j]) and res[-1] != queries[i]:
                    res.append(queries[i])
        
        return res[1:]
