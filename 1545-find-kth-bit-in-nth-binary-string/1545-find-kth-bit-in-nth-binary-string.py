class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # def reverse(st):
        #     return st[::-1]
        
        # def invert(st):
        #     st = st.replace("1", "_")
        #     st = st.replace("0", "1")
        #     st = st.replace("_", "0")
        #     return st
        
        # def findS(x):
        #     if x == 0:
        #         return "0"
            
        #     S = findS(x-1)
        #     return S + "1" + reverse(invert(S))
        
        # binary = findS(n-1)
        # return binary[k-1]


        if n == 1:
            return "0"
        
        length = (1 << n) - 1
        mid = length // 2 + 1

        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n-1, k)
        
        mirrored = length - k + 1
        bit = self.findKthBit(n-1, mirrored)

        return "1" if bit == "0" else "0"
