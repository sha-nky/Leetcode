class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            if n == 1:
                return False
            
            for i in range(2, n//2 + 1):
                if n % i == 0:
                    return False
            return True
        
        count = 0
        for num in range(left, right + 1):
            if isPrime(num.bit_count()):
                count += 1
        return count
