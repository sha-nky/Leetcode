class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(i, k, temp):
            if k==0:
                res.append(temp[:])
                return
            if k<0:
                return
            for j in range(i, n):
                temp.append(candidates[j])
                dfs(j, k-candidates[j], temp)
                temp.pop()
        
        dfs(0, target, [])
        return res
