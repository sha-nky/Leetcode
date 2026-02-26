class Solution:
    def numSteps(self, s: str) -> int:
        a = int(s,2)
        count = 0
        while a!= 1 :
            count+=1
            if a%2==0:
                a=a//2
            else:
                a=a+1
        return count;